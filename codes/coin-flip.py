import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
np.random.seed(42)

#bernoulli test
n=500
pcoin=0.62
results = st.bernoulli(pcoin).rvs(n)
h = sum(results)
print("we observed %s heads out of %s"%(h,n))

#null hypothesis
p = 0.5
rv = st.binom(n,p)
mu = rv.mean()
sd = rv.std()
print("The expected distribution for a fair coin is mu=%s, sd=%s"%(mu,sd))

#binomial test
print("binomial test p-value: %s"%st.binom_test(h, n, p))

#z binom_test
z = (h-0.5-mu)/sd
print("normal approximation p-value: - %s"%(2*(1 - st.norm.cdf(z))))

#baysenian
fig  = plt.figure()
ax = fig.add_subplot(111)

a, b = 10, 10
prior = st.beta(a, b)
post = st.beta(h+a, n-h+b)
ci = post.interval(0.95)
map_ =(h+a-1.0)/(n+a+b-2.0)

xs = np.linspace(0, 1, 100)
ax.plot(prior.pdf(xs), label='Prior')
ax.plot(post.pdf(xs), label='Posterior')
ax.axvline(mu, c='red', linestyle='dashed', alpha=0.4)
ax.set_xlim([0, 100])
ax.axhline(0.3, ci[0], ci[1], c='black', linewidth=2, label='95% CI');
ax.axvline(n*map_, c='blue', linestyle='dashed', alpha=0.4)
ax.legend()
plt.show()
