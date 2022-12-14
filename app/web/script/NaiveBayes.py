import numpy as np

class NaiveBayes():

    def __init__(self, c = 1):
        self.c = c
        self.x_counts = list()
        self.y_counts = np.array([])

    def train(self, x_train, y_train):

        ys, self.y_counts = np.unique(y_train, return_counts=True)

        x_transpose = np.transpose(x_train)
        x_uniques = list()

        for i in range(len(x_transpose)):
            xs = np.unique(x_transpose[i])
            x_uniques.append(xs.tolist())

        # Ambil jumlah baris dan kolom x_train
        rows, cols = x_train.shape

        for y_item, y_index in enumerate(ys):
            prob = list()
            for x_unique_index, x_unique_item in enumerate(x_uniques):
                temp = list()
                for x_unique in x_unique_item:
                    x_count = 0
                    for x_train_index, x_train_item in enumerate(x_train):
                        if x_train_item[x_unique_index] == x_unique and y_train[x_train_index] == y_item:
                            x_count += 1
                    temp.append(x_count)
                prob.append(temp)
            self.x_counts.append(prob)     
            
    def predict(self, xs):
        y_probs = list()
        laplace_check = [False, False]
        
        # Cek frekuensi 0   
        for x_counts_index, x_count in enumerate(self.x_counts):
            for x_count_index, x_count_col in enumerate(x_count): 
                if x_count_col[xs[x_count_index]] == 0:
                    laplace_check[x_counts_index] = True
                    break
        
        # Hitung probabilitas
        for x_counts_index, x_count in enumerate(self.x_counts):
            y_prob = 1
            if laplace_check[x_counts_index]:
                for x_count_index, x_count_col in enumerate(x_count): 
                    y_prob *= ((x_count_col[xs[x_count_index]] + self.c) / 
                    (self.y_counts[x_counts_index] + self.c * len(self.x_counts[0])))
            else:
                for x_count_index, x_count_col in enumerate(x_count): 
                    y_prob *= ((x_count_col[xs[x_count_index]]) / 
                    (self.y_counts[x_counts_index]))
            y_probs.append(y_prob)

        # Menentukan hasil klasifikasi
        max_index = y_probs.index(max(y_probs))

        return max_index, y_probs
