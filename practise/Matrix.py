import array
import numpy as np

class AHP:
    #信息传入和准备
    def __init__(self,array):
        self.array = array
        #记录矩阵大小
        self.n=array.shape[0]
        # 初始化RI值，用于一致性检验
        self.RI_list = [0, 0, 0.52, 0.89, 1.12, 1.26, 1.36, 1.41, 1.46, 1.49, 1.52, 1.54, 1.56, 
        1.58,1.59]
        #矩阵的特征值和特征向量
        self.eig_val,self.eig_vector = np.linalg.eig(self.array)
        #矩阵的最大特征值
        self.max_eig_val = np.max(self.eig_val)
        #矩阵最大特征值对应的特征向量
        self.max_eig_vector = self.eig_vector[:,np.argmax(self.eig_val)].real
        #矩阵的一致性指标CI
        self.CI_val = (self.max_eig_val - self.n) / (self.n - 1)
        #矩阵的一致性比例CR
        self.CR_val = self.CI_val / (self.RI_list[self.n - 1])


    def test_consist(self):
        #打印矩阵的一致性指标CI和一致性比例CR
        print("判断矩阵的CI值为:",self.CI_val)
        print("判断矩阵的CR值为:",self.CR_val)

        if self.n == 2 : #当只有两个子因素时不包含一致性问题
            print("仅包含两个子因素,不存在一致性问题")
        else:
            if self.CR_cal < 0.1:
                print("判断矩阵的CR值为\n",self.CR_val)
                print("通过一致性检验")
                return True

            else:
                print("未通过一致性检验")
                return False



    def cal_weight_by_arithemic_method(self):           #算数平均法
        #求矩阵的每列的和  axis=0按列求和    axis=1按行求和
        col_sum = np.sum(self.array,axis=0)
        #判断矩阵按照列归一化处理
        #归一化的目的是把一组数据变为总和为1的比例
        array_normed = self.array / col_sum
        #计算权重向量
        array_weight1 = np.sum(array_normed,axis=1) / self.n
        #打印权重向量
        print("算术平均法计算得到的权重向量为:\n",array_weight1)
        #返回值
        return array_weight1


    def cal_weight_by_geometric_method(self):           #几何平均法
        #求矩阵的每列的积
        col_product = np.prod(self.array,axis=0)
        #将得到的积向量的每个分量进行开n次方
        array_power=np.power(col_product,1/self.n)
        #将列向量归一化
        array_weight2=array_power/np.sum(array_power)
        #打印权重向量
        print("几何平均法计算得到的权重向量为:\n",array_weight2)
        #返回权重向量的值
        return array_weight2

    
    def cal_weight_by_eigenvalue_method(self):          #特征值法
        
        # 1. 对矩阵做特征值分解，得到所有特征值和特征向量
        eig_vals, eig_vecs = np.linalg.eig(self.array)
        # 2. 取特征值的实部（消除数值误差导致的虚部）
        eig_vals_real = np.real(eig_vals)
        # 3. 找到最大特征值对应的索引
        max_eig_idx = np.argmax(eig_vals_real)
        # 4. 取最大特征值对应的特征向量（同样取实部）
        max_eig_vector = np.real(eig_vecs[:, max_eig_idx])
        # 5. 对特征向量做归一化（元素和为1），得到权重向量
        array_weight3 = max_eig_vector / np.sum(max_eig_vector)
        # 打印权重向量（此时是3个元素的向量）
        print("特征值法计算得到的权重向量为:\n", array_weight3)
        return array_weight3

if __name__ == "__main__":
    #给出判断矩阵
    b = np.array([[1,1/3,1/8],[3,1,1/3],[8,3,1]])

    #算术平均法求权重
    weight1 = AHP(b).cal_weight_by_arithemic_method()

    #几何平均法求权重
    weight2 = AHP(b).cal_weight_by_geometric_method()

    #特征值法求权重
    weight3 = AHP(b).cal_weight_by_eigenvalue_method()
