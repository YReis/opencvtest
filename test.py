import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_circles

# Create a simple dataset
X, y = make_circles(n_samples=100, factor=.1, noise=.1, random_state=42)

# SVM models with different gamma values
models = (svm.SVC(kernel='rbf', gamma=0.1),
          svm.SVC(kernel='rbf', gamma=1))
models = (clf.fit(X, y) for clf in models)

# Title for the plots
titles = ('SVM with gamma=0.1',
          'SVM with gamma=1')

# Set-up 2x2 grid for plotting
fig, sub = plt.subplots(1, 2, figsize=(8, 4))

# Plot each model
for clf, title, ax in zip(models, titles, sub.flatten()):
    # Plot the decision boundary
    xlim = (-1.5, 1.5)
    ylim = (-1.5, 1.5)
    xx, yy = np.meshgrid(np.linspace(*xlim, num=500),
                         np.linspace(*ylim, num=500))
    Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    ax.contourf(xx, yy, Z, levels=np.linspace(Z.min(), Z.max(), 100), cmap=plt.cm.coolwarm, alpha=0.8)

    # Plot the training points
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k')
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(title)

plt.tight_layout()
plt.show()
