import pandas as pd
import numpy as np
from scipy.stats import dirichlet
import warnings
warnings.filterwarnings('ignore')

df = pd.read_excel(r"C:\Users\29418\Desktop\important.xlsx")
df['season'] = df['season'].astype(int)
all_columns = df.columns.tolist()

# 自动识别“周-评委”列（兼容week1~week30等任意周数）
week_judge_cols = [col for col in all_columns if 'week' in col.lower() and 'judge' in col.lower()]
if not week_judge_cols:
    raise ValueError("数据中未找到'week+judge'格式的列(如week1_judge1),请检查列名！")

# 提取周并按数字排序（优化：避免week10排在week2前面）
all_weeks = list(set([col.split('_')[0] for col in week_judge_cols]))
all_weeks.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))  # 按周数数字排序
print(f"自动识别：总周数={len(all_weeks)}，周列表={all_weeks}")

# 按季存储“每周评委列”（优化：增加进度打印）
season_week_judges = {}
total_seasons = df['season'].nunique()
for idx, (season, df_season) in enumerate(df.groupby('season'), 1):
    season_week_judges[season] = {}
    for week in all_weeks:
        week_cols = [col for col in week_judge_cols if col.startswith(week) and col in df_season.columns]
        if week_cols:
            season_week_judges[season][week] = week_cols
    print(f"  处理季{season}（{idx}/{total_seasons}）：有效周数={len(season_week_judges[season])}")


season_week_data = {}
print(f"\n🔄 开始整理按季按周数据...")
for season in season_week_data:
    season_week_data[season] = {}

for season in season_week_judges:
    df_season = df[df['season'] == season].copy()
    season_week_data[season] = {}
    for week in season_week_judges[season]:
        judge_cols = season_week_judges[season][week]
        # 筛选本周存活选手（评委分不全为0）
        df_week = df_season[df_season[judge_cols].sum(axis=1) > 0].copy()
        if len(df_week) < 2:
            continue
        
        # 计算评委总分（优化：避免总和为0）
        df_week['judge_total_week'] = df_week[judge_cols].sum(axis=1)
        judge_total_sum = df_week['judge_total_week'].sum()
        if judge_total_sum == 0:
            df_week['judge_pct'] = 0.0
        else:
            df_week['judge_pct'] = df_week['judge_total_week'] / judge_total_sum
        
        # 标记淘汰者（优化：处理无下一周数据的情况）
        next_week_num = int(''.join(filter(str.isdigit, week))) + 1
        next_week = f'week{next_week_num}'
        next_week_judge_cols = [col for col in week_judge_cols if col.startswith(next_week) and col in df_week.columns]
        df_week['is_eliminated'] = 0
        if next_week_judge_cols:
            df_week['is_eliminated'] = (df_week[next_week_judge_cols].sum(axis=1) == 0).astype(int)
        
        season_week_data[season][week] = df_week

# 统计有效数据（优化：显示最终整理结果）
valid_seasons = len([s for s in season_week_data if len(season_week_data[s]) > 0])
valid_weeks = sum(len(v) for v in season_week_data.values())
print(f"✅ 数据整理完成！有效季数={valid_seasons}，有效周数={valid_weeks}")


n_mc = 100
valid_fan_votes = {}
print(f"生成100组符合条件的粉丝投票...")

for season in season_week_data:
    if len(season_week_data[season]) == 0:
        continue
    valid_fan_votes[season] = {}
    print(f"\n=== 处理季{season} ===")
    total_weeks_season = len(season_week_data[season])
    
    for week_idx, week in enumerate(season_week_data[season], 1):
        df_week = season_week_data[season][week]
        n_contestants = len(df_week)
        valid_votes = []
        max_attempts = 10000  # 防止无限循环
        attempts = 0
        
        # 生成投票（优化：增加最大尝试次数，避免卡住）
        while len(valid_votes) < n_mc and attempts < max_attempts:
            fan_vote = dirichlet.rvs(alpha=[1]*n_contestants, size=1)[0]
            # 安全赋值：按当前行索引构造Series，避免索引对齐导致错位
            df_week['fan_pct'] = pd.Series(fan_vote, index=df_week.index)
            # 合并得分（权重w可按需调整）
            w = 0.5
            df_week['total_score'] = w * df_week['judge_pct'] + (1 - w) * df_week['fan_pct']
            # 验证淘汰结果
            min_score = df_week['total_score'].min()
            min_contestants = df_week[df_week['total_score'] == min_score]
            if min_contestants['is_eliminated'].sum() >= 1:
                valid_votes.append(fan_vote)
            attempts += 1
        
        # 处理极端情况（若未生成足够投票，用已有投票填充）
        if len(valid_votes) == 0:
            # 回退：若没有一组符合条件的投票，则直接生成n_mc组Dirichlet样本作为备用（可能不满足淘汰条件）
            fallback_votes = dirichlet.rvs(alpha=[1]*n_contestants, size=n_mc)
            valid_votes = [v for v in fallback_votes]
        elif len(valid_votes) < n_mc:
            times = n_mc // len(valid_votes)
            rem = n_mc % len(valid_votes)
            valid_votes = valid_votes * times + valid_votes[:rem]
        
        valid_fan_votes[season][week] = np.array(valid_votes)
        print(f"  周{week}（{week_idx}/{total_weeks_season}）：生成{len(valid_votes)}组投票（选手数={n_contestants}，评委数={len(season_week_judges[season][week])}）")


result_list = []
for season in valid_fan_votes:
    for week in valid_fan_votes[season]:
        df_week = season_week_data[season][week].reset_index(drop=True)
        votes = valid_fan_votes[season][week]
        judge_count = len(season_week_judges[season][week])
        
        # 添加100组投票
        for mc_idx in range(n_mc):
            df_week[f'fan_pct_mc{mc_idx+1}'] = votes[mc_idx]
        
        # 添加标识列
        df_week['season'] = season
        df_week['week'] = week
        df_week['judge_count_week'] = judge_count
        
        result_list.append(df_week)

# 合并并调整列顺序（优化：核心列在前）
final_result = pd.concat(result_list, ignore_index=True)
# 定义列顺序：标识列 → 评委相关 → 淘汰状态 → 100组投票
core_order = ['season', 'week', 'judge_count_week', 'celebrity_name', 
              'judge_total_week', 'judge_pct', 'is_eliminated']
mc_cols = [col for col in final_result.columns if 'fan_pct_mc' in col]
other_cols = [col for col in final_result.columns if col not in core_order + mc_cols]
final_result_output = final_result[core_order + other_cols + mc_cols]

# 保存（优化：文件名更规范）
output_path = r"C:\Users\29418\Desktop\按季按周_100组粉丝投票_优化版.xlsx"
final_result_output.to_excel(output_path, index=False)

