import numpy as np
np.random.seed(0)


class sampling:
    def __init__(self, data, n):
        self.n = n
        self.s = np.random.choice(data, n)
        self.mean, self.var = self.get_mean_and_variance()

    def __str__(self):
        print('Randomly sample {} samples from population : {}'.format(self.n, ', '.join(map(str, self.s))))
        print()
        print(f'Estimate mean in sample distribution: {self.mean}')
        print(f'Estimate variance in sample distribution: {self.var}')

        return ''

    def get_mean_and_variance(self):
        def get_mean():
            return np.round_(np.sum(self.s) / self.n, 1)

        def get_var():
            res = np.sum((self.s - self.mean) ** 2) / (self.n - 1)
            res = np.round_(res, 2)
            return res

        self.mean = get_mean()
        self.var = get_var()

        return [self.mean, self.var]

    def estimate_population_mean_and_variance(self, population_var):
        def estimate_population_mean():
            StDev = np.sqrt(population_var)

            min_val = self.mean - 1.96 * StDev / np.sqrt(self.n)
            max_val = self.mean + 1.96 * StDev / np.sqrt(self.n)

            min_val = np.round_(min_val, 2)
            max_val = np.round_(max_val, 2)
            return min_val, max_val

        def estimate_population_var():
            min_val = (self.n - 1) * self.var / chi[self.n][0]
            max_val = (self.n - 1) * self.var / chi[self.n][1]

            min_val = np.round_(min_val, 2)
            max_val = np.round_(max_val, 2)
            return min_val, max_val

        chi = {10: [19.023, 2.7], 30: [45.722, 16.047], 61: [83.298, 40.482]}

        epm = estimate_population_mean()
        print(f'Using sample distribution,Estimate population mean with 95% confidence interval : {epm[0]} < μ < {epm[1]}')

        epv = estimate_population_var()
        print(f'Using sample distribution, Estimate population variance with 95% confidence interval : {epv[0]} < σ^2 < {epv[1]}')

    def estimate_population_mean_t_distribution(self):
        StDev = np.sqrt(self.var)

        min_val = self.mean - 2.447 * StDev / np.sqrt(self.n)
        max_val = self.mean + 2.447 * StDev / np.sqrt(self.n)

        min_val = np.round_(min_val, 2)
        max_val = np.round_(max_val, 2)

        print(f'Estimate population mean with 95% confidence interval in t-distribution : {min_val} < μ < {max_val}')
