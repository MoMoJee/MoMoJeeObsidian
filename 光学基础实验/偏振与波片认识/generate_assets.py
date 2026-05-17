from pathlib import Path
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

I0 = 10.04
THETA_Q = np.arange(0, 360, 10)
QUARTER = {"0": [0.00, 0.22, 0.96, 2.00, 3.32, 4.79, 6.21, 7.42, 8.08, 8.30, 8.16, 7.54, 6.68, 5.48, 3.83, 2.42, 1.13, 0.33, 0.00, 0.18, 0.86, 1.90, 3.26, 4.65, 6.11, 7.33, 8.22, 8.60, 8.46, 7.85, 6.67, 5.23, 3.67, 2.27, 1.12, 0.34], "30": [2.96, 2.43, 2.12, 2.10, 2.32, 2.71, 3.38, 4.16, 4.89, 5.52, 6.01, 6.24, 6.44, 6.41, 5.90, 5.35, 4.44, 3.70, 2.94, 2.41, 2.07, 2.01, 2.24, 2.64, 3.25, 3.92, 4.71, 5.38, 5.98, 6.36, 6.48, 6.27, 5.83, 5.21, 4.44, 3.68], "45": [4.08, 4.12, 4.16, 4.26, 4.36, 4.43, 4.53, 4.70, 4.72, 4.71, 4.67, 4.58, 4.59, 4.56, 4.43, 4.31, 4.15, 4.06, 4.00, 3.99, 4.03, 4.09, 4.23, 4.28, 4.41, 4.48, 4.57, 4.61, 4.64, 4.63, 4.58, 4.47, 4.37, 4.25, 4.17, 4.10], "75": [1.09, 1.84, 3.09, 4.57, 5.94, 7.10, 8.07, 8.71, 8.69, 8.26, 7.49, 6.32, 5.10, 3.77, 2.48, 1.44, 0.80, 0.07, 1.03, 1.85, 2.93, 4.26, 5.71, 6.81, 7.86, 8.43, 8.58, 8.22, 7.42, 6.28, 4.91, 3.53, 2.22, 1.28, 0.75, 0.68]}
THETA_H = np.arange(0, 361, 10)
HALF = {"0": [0.00, 0.38, 1.25, 2.56, 4.18, 5.99, 7.52, 9.01, 9.71, 9.85, 9.45, 8.52, 7.34, 5.87, 4.07, 2.38, 1.05, 0.24, 0.21, 0.34, 1.23, 2.51, 4.19, 5.77, 7.35, 8.61, 9.49, 9.75, 9.43, 8.61, 7.22, 5.62, 3.94, 2.27, 1.05, 0.24, 0.00], "30": [7.19, 5.54, 3.82, 2.26, 0.97, 0.23, 0.04, 0.44, 1.39, 2.67, 4.22, 5.81, 7.59, 8.96, 9.81, 10.04, 9.56, 8.53, 7.00, 5.31, 3.64, 2.07, 0.91, 0.18, 0.03, 0.43, 1.40, 2.67, 4.22, 5.91, 7.43, 8.26, 9.62, 9.86, 9.55, 8.52, 7.21], "45": [10.03, 9.76, 8.71, 7.45, 5.71, 3.90, 2.31, 1.08, 0.29, 0.04, 0.33, 1.17, 2.49, 4.17, 5.89, 7.49, 8.71, 9.55, 9.81, 9.42, 8.45, 7.14, 5.21, 3.95, 2.31, 1.06, 0.28, 0.05, 0.38, 1.27, 2.55, 4.15, 5.81, 7.42, 8.75, 9.69, 10.04], "75": [2.58, 4.22, 5.91, 7.56, 8.88, 9.58, 9.78, 9.58, 8.58, 7.22, 5.70, 3.94, 2.50, 1.13, 0.25, 0.01, 0.34, 1.18, 2.45, 4.05, 5.71, 7.34, 8.59, 9.39, 9.71, 9.36, 8.49, 7.22, 5.63, 3.80, 2.27, 1.02, 0.25, 0.01, 0.35, 1.20, 2.54]}


def normalized(values):
    return np.array(values, dtype=float) / I0


def write_table(path, theta, data, start, stop):
    lines = [r"\begin{tabular}{ccccc}", r"  \toprule", r"  $\theta/^{\circ}$ & $I(0^{\circ})$/mW & $I(30^{\circ})$/mW & $I(45^{\circ})$/mW & $I(75^{\circ})$/mW \\", r"  \midrule"]
    for idx in range(start, stop):
        row = [f"{theta[idx]}"] + [f"{data[key][idx]:.2f}" for key in ("0", "30", "45", "75")]
        lines.append("  " + " & ".join(row) + r" \\")
    lines.extend([r"  \bottomrule", r"\end{tabular}"])
    path.write_text("\n".join(lines), encoding="utf-8")


def plot_cartesian(path, theta, data, title):
    fig, ax = plt.subplots(figsize=(7.2, 4.4), dpi=160)
    for key, color in (("0", "#1f77b4"), ("30", "#d62728"), ("45", "#2ca02c")):
        ax.plot(theta, normalized(data[key]), marker="o", markersize=3.2, linewidth=1.5, color=color, label=f"{key} deg")
    ax.set(xlabel="theta / deg", ylabel="I / I0", title=title, xlim=(0, theta[-1]), ylim=(0, 1.05))
    ax.grid(alpha=0.28)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def plot_polar(path, theta, data, title):
    fig = plt.figure(figsize=(6.2, 5.2), dpi=160)
    ax = fig.add_subplot(111, projection="polar")
    for key, color in (("0", "#1f77b4"), ("30", "#d62728"), ("45", "#2ca02c")):
        degrees = theta if theta[-1] == 360 else np.append(theta, 360)
        radius = normalized(data[key]) if theta[-1] == 360 else np.append(normalized(data[key]), normalized(data[key])[0])
        ax.plot(np.deg2rad(degrees), radius, linewidth=1.5, color=color, label=f"{key} deg")
    ax.set_title(title, va="bottom")
    ax.set_rmax(1.0)
    ax.grid(alpha=0.35)
    ax.legend(loc="lower left", bbox_to_anchor=(1.02, -0.02), frameon=False)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def plot_cos2(path, theta, values, title):
    x = np.cos(np.deg2rad(theta)) ** 2
    y = normalized(values)
    order = np.argsort(x)
    fit = np.polyfit(x, y, 1)
    y_fit = np.polyval(fit, x)
    r2 = 1 - np.sum((y - y_fit) ** 2) / np.sum((y - y.mean()) ** 2)
    fig, ax = plt.subplots(figsize=(5.5, 4.2), dpi=160)
    ax.scatter(x, y, s=18, color="#1f77b4")
    ax.plot(x[order], y_fit[order], color="#d62728", linewidth=1.4, label=fr"fit: y={fit[0]:.3f}x+{fit[1]:.3f}, R^2={r2:.3f}")
    ax.set(xlabel=r"cos^2(theta)", ylabel="I / I0", title=title, xlim=(0, 1.0), ylim=(0, 1.05))
    ax.grid(alpha=0.28)
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    return fit, r2


def main():
    root = Path(__file__).resolve().parent
    generated = root / "generated"
    plots = root / "plots"
    generated.mkdir(exist_ok=True)
    plots.mkdir(exist_ok=True)
    write_table(generated / "quarter_table_a.tex", THETA_Q, QUARTER, 0, 18)
    write_table(generated / "quarter_table_b.tex", THETA_Q, QUARTER, 18, 36)
    write_table(generated / "half_table_a.tex", THETA_H, HALF, 0, 18)
    write_table(generated / "half_table_b.tex", THETA_H, HALF, 18, len(THETA_H))
    plot_cartesian(plots / "quarter_cartesian.png", THETA_Q, QUARTER, "Quarter-wave plate: I/I0 vs theta")
    plot_polar(plots / "quarter_polar.png", THETA_Q, QUARTER, "Quarter-wave plate polar plot")
    plot_cartesian(plots / "half_cartesian.png", THETA_H, HALF, "Half-wave plate: I/I0 vs theta")
    plot_polar(plots / "half_polar.png", THETA_H, HALF, "Half-wave plate polar plot")
    for key in ("0", "30", "45"):
        fit_q, r2_q = plot_cos2(plots / f"quarter_cos2_{key}.png", THETA_Q, QUARTER[key], f"Quarter-wave plate {key} deg")
        fit_h, r2_h = plot_cos2(plots / f"half_cos2_{key}.png", THETA_H, HALF[key], f"Half-wave plate {key} deg")
        print(f"quarter {key} deg: min={normalized(QUARTER[key]).min():.3f}, max={normalized(QUARTER[key]).max():.3f}, peak={THETA_Q[int(np.argmax(QUARTER[key]))]} deg, R2={r2_q:.3f}")
        print(f"half {key} deg: min={normalized(HALF[key]).min():.3f}, max={normalized(HALF[key]).max():.3f}, peak={THETA_H[int(np.argmax(HALF[key]))]} deg, R2={r2_h:.3f}")


if __name__ == "__main__":
    main()