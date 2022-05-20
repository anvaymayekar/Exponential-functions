import matplotlib.pyplot as plt

black = '#262625'
# black = '#21211f'


def exponential(start, step=1, limit=10, constant=0, power=2):
    base = []

    bound = step * limit
    stop = bound + 1
    for i in range(bound, - stop, -step):
        x = i
        y = pow(i, power) + constant
        base.append((x, y))

    fx = tuple(map(lambda x: x[0], base))
    fy = tuple(map(lambda x: x[1], base))
    print(base)
    plt.style.use('bmh')
    plt.rcParams.update({
        "lines.color": "white",
        "patch.edgecolor": "white",
        "text.color": "white",
        "axes.facecolor": black,
        "axes.edgecolor": "white",
        "axes.labelcolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "grid.color": "white",
        "figure.facecolor": black,
        "figure.edgecolor": black,
        "savefig.facecolor": black})
    plt.plot(fx, fy, color='#077bef', label='$curve$')
    plt.axvline(color='#fff', linestyle='dashed')
    plt.axhline(color='#fff', linestyle='dashed')
    plt.scatter(fx, fy, c='#196CE6', s=20, label='$points$')
    plt.xlabel(
        f'$X-axis$\n $x_s={start}, x_l={limit}, x_i={step}$', style='oblique')
    plt.ylabel('$Y-axis$', style='oblique')
    k_text = f' + {constant}' if constant > 1 else ''
    plt.title(
        f"$Exponential functions$\n $y = f(x) = x^{power}{k_text}$", style='oblique')
    plt.grid(True)
    plt.legend(loc='center right', )
    # plt.savefig('F:\Sublime Codes\Anvay Algorithms\Math\demo4.png')
    plt.show()


e = exponential(2, 2, 20)
