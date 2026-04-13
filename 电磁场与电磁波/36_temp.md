# 3.6.1 直角坐标系中的分离变量法

![image](images/6eccec7af0ed28db167ece2ac7a1b360f45a6ab1bb8e0eed71715739bd9e27f2.jpg)


$$
\frac {d ^ {2} f}{d x ^ {2}} = - k _ {x} ^ {2} f, \frac {d ^ {2} g}{d y ^ {2}} = - k _ {y} ^ {2} g, \frac {d ^ {2} h}{d z ^ {2}} = - k _ {z} ^ {2} h
$$

$$
k _ {x} ^ {2} + k _ {y} ^ {2} + k _ {z} ^ {2} = 0 \quad \frac {d ^ {2} f}{d x ^ {2}} = - k _ {x} ^ {2} f
$$

$$
f (x) = \left\{ \begin{array}{c c} A _ {1} x + A _ {2} & k _ {x} = \mathbf {0} \\ A _ {1} \sin k _ {x} x + A _ {2} \cos k _ {x} x & k _ {x} ^ {2} > \mathbf {0} \\ A _ {1} \overline {{\sinh | k _ {x} | x}} + A _ {2} \overline {{\cosh | k _ {x} | x}} = A _ {1} ^ {\prime} e ^ {| k _ {x} | x} + A _ {2} ^ {\prime} e ^ {- | k _ {x} | x} & k _ {x} ^ {2} <   \mathbf {0} \end{array} \right.
$$

双曲正弦

双曲余弦

同样对于 $g ( y )$ 和 $h ( z )$ 也有同样形式的解。

则拉普拉斯方程的解为：

$$
\varphi (x, y, z) = f (x) g (y) h (z)
$$

$\overline { { k _ { x } ^ { 2 } , k _ { y } ^ { 2 } , k _ { z } ^ { 2 } } }$ 不能同时为正，或者为负， $f ( x ) , g ( y ) , h ( z )$ 不能都取相同形式的解。

在具体问题中，通常根据边界条件来选择函数 $f ( x ) , g ( y ) , h ( z )$ 的表达式形式，有以下几种情况：

（1）对于有两个零值边界的方向，其对应的函数一般可以取三角函数形式。

（2）对于单零值边界的方向，对应的函数一般取双曲函数形式。

（3）有无限远边界的方向，一般取指数函数形式。

（4）若位函数与某一坐标变量无关，则该变量对应的函数应取成常数，考虑到其他变量对应解中均含有待定系数，故该常数一般取作1。

# 满足齐次边界条件的分离常数可以取一系列的特殊值

$$
k _ {x i}, k _ {y i}, k _ {z i} \quad (i = 1, 2, 3 \dots)
$$

这些特殊值称为本征值，本征值对应的函数称为本征函数或本征解。根据叠加原理，所有本征解的线性叠加构成满足拉普拉斯方程的通解。

$$
\varphi (x, y, z) = \sum_ {i = 1} ^ {n} \varphi_ {i} (x, y, z) = \sum_ {i = 1} ^ {n} f _ {i} (x) g _ {i} (y) h _ {i} (z)
$$

在许多问题中，单一本征函数不能满足所给边界条件，而级数形式的通解则可以满足单个解函数所无法满足的边界条件。

（1）若 $\varphi = \varphi ( x , y )$ 

$$
\left\{ \begin{array}{l} \frac {d ^ {2} X}{d x ^ {2}} + \alpha X = 0 \\ \frac {d ^ {2} Y}{d y ^ {2}} + \beta Y = 0 \end{array} \right.
$$

$$
\alpha = - k ^ {2}, \beta = k ^ {2} \quad \alpha + \beta = 0
$$

$$
X (x) = A e ^ {k x} + B e ^ {- k x}
$$

$$
Y (y) = C \sin k y + D \cos k y
$$

（2）若 $\varphi = \varphi ( x )$ ，与 无关。

$$
\frac {d ^ {2} \varphi}{d x ^ {2}} = 0 \quad \varphi = A x + B
$$

![image](images/73966c32a93a037bae6fcca131cf19348d7eab1f1cad5dab2045d5c386a2716b.jpg)


# ❖ 解题步骤

1.选择坐标系和电势参考点

坐标系选择主要根据区域中分界面形状，参考点主要根据电荷分布是有限还是无限；

2.分析对称性、分区写出拉普拉斯方程在所选坐标系中的通解；

3. 根据具体条件确定常数

（1）外边界条件： 电荷分布有限 $\left. \varphi \right| _ { \infty } = 0$ 

注意：边界条件和边值关系是相对的。导体边界可视为外边界，给定 $\left. \varphi \right| _ { S }$ （接地 $\varphi _ { \vert _ { S } } = 0 )$ ，或给定总电荷 Q，或给定 

电荷分布无限，电势参考点一般选在有限区。如均匀场中， $\begin{array} { r l } { \vec { E } = E _ { 0 } \vec { e } _ { z } } & { { } \varphi \big \rvert _ { \infty }  - E _ { 0 } r \cos \theta = - E _ { 0 } z } \end{array}$ $\vec { E } = E _ { 0 } \vec { e } _ { z }$ （直角坐标或柱坐标） ? 电势可选在坐标原点。

（2）内部边值关系：介质分界面上

$$
\left. \varphi_ {1} \right| _ {S} = \left. \varphi_ {2} \right| _ {S} \qquad \left. \varepsilon_ {1} \frac {\partial \varphi_ {1}}{\partial n} \right| _ {S} = \left. \varepsilon_ {2} \frac {\partial \varphi_ {2}}{\partial n} \right| _ {S}
$$

一般讨论分界面无自由电荷的情况

例3.6.1 无限长的矩形金属导体槽上有一盖板，盖板与金属槽绝缘，盖板电位为 $U _ { \mathbf { 0 } }$ ，金属槽接地，横截面如图所示，试计算此导体槽内的电位分布。

![image](images/5ca70286c7af57efae2acf0e6e78506b34467384652841f3a057fbc0851ed364.jpg)


# 3.6.2 圆柱坐标系中的分离变量法

$$
\frac {1}{r} \frac {\partial}{\partial r} (r \frac {\partial \varphi}{\partial r}) + \frac {1}{r ^ {2}} \frac {\partial^ {2} \varphi}{\partial \theta^ {2}} + \boxed {\frac {\partial^ {2} \varphi}{\partial z ^ {2}}} = 0
$$

只讨论二维平面场

$$
\frac {1}{r} \frac {\partial}{\partial r} (r \frac {\partial \varphi}{\partial r}) + \frac {1}{r ^ {2}} \frac {\partial^ {2} \varphi}{\partial \theta^ {2}} = 0
$$

设解的形式为：

$$
\varphi = f (r) g (\theta)
$$

$$
\frac {g (\theta)}{r} \frac {\partial}{\partial r} (r \frac {f (r)}{\partial r}) + \frac {f (r)}{r ^ {2}} \frac {\partial^ {2} g (\theta)}{\partial \theta^ {2}} = 0
$$

$$
\left(\frac {r ^ {2}}{f (r) g (\theta)} \right.
$$

$$
\frac {\frac {r}{f (r)} \frac {\partial}{\partial r} (r \frac {f (r)}{\partial r}) + \frac {1}{g (\theta)} \frac {\partial^ {2} g (\theta)}{\partial \theta^ {2}} = 0}{\downarrow_ {\gamma^ {2}}}
$$

$$
\frac {d ^ {2} g (\theta)}{d \theta^ {2}} + \gamma^ {2} g (\theta) = 0 \Longrightarrow g (\theta) = A \sin (\gamma \theta) + B \cos (\gamma \theta)
$$

$$
\varphi \left[ \gamma (\theta + 2 \pi) \right] = \varphi (\gamma \theta) \quad \gamma = n \quad n \text {为 整 数}
$$

$$
g (\theta) = A \sin (n \theta) + B \cos (n \theta) \quad r \frac {a}{d r} \left(r \frac {f (r)}{d r}\right) - n ^ {2} f (r) = 0
$$

$$
\begin{array}{l} r ^ {2} \frac {d ^ {2} f (r)}{d r ^ {2}} + r \frac {d f (r)}{d r} - n ^ {2} f (r) = 0 \\ n = 0 \quad f (r) = C _ {0} + D _ {0} \ln r \end{array} \quad \begin{array}{l} f (r) = C r ^ {n} + D r ^ {- n} \\ \text {欧 拉 方 程} \end{array}
$$

$$
\varphi = \sum_ {n = 1} ^ {\infty} \left[ A _ {n} \sin (n \theta) + B _ {n} \cos (n \theta) \right] \left(C _ {n} r ^ {n} + D _ {n} r ^ {- n}\right)
$$

例：一半径为 a，介电常数为 $\mathcal { E }$ 的无 限长电介质圆柱，柱轴沿 $\vec { e } _ { z }$ 方向， $\vec { e } _ { x }$ ex 方向上有一外加均匀电场 $\vec { E } _ { 0 }$ ，求空间电势分布和柱面上的束缚电荷分布。

解：(1)边界为柱面,选柱坐标系。均匀场电势在无穷远处不为零，故参考点选在有限区域，例如可选在坐标原点

![image](images/343805aac3a5b328c5872afc6f70beb46cb0f7aa6d083a5b5d9e2da360cdfabc.jpg)


(2) 考虑对称性电势与z无关，设柱内电势为 $\varphi _ { 1 }$ ，柱外为 $\varphi _ { 2 }$ 它们分别满足 $\nabla ^ { 2 } \varphi _ { 1 } = 0 ( 0 < r < a )$ , $\nabla ^ { 2 } \varphi _ { 2 } = 0 \ ( r > a )$ 。通解为：

$$
\varphi_ {1} = \sum_ {n = 1} ^ {\infty} \left[ r ^ {n} \left(A _ {n} ^ {(1)} \sin n \theta + B _ {n} ^ {(1)} \cos n \theta\right) + r ^ {- n} \left(C _ {n} ^ {(1)} \sin n \theta + D _ {n} ^ {(1)} \cos n \theta\right) \right]
$$

$$
\varphi_ {1} = \sum_ {n = 1} ^ {\infty} [ r ^ {n} (A _ {n} ^ {(1)} \sin n \theta + B _ {n} ^ {(1)} \cos n \theta) + r ^ {- n} (C _ {n} ^ {(1)} \sin n \theta + D _ {n} ^ {(1)} \cos n \theta) ]
$$

a<r<8 

$$
\varphi_ {2} = \sum_ {n = 1} ^ {\infty} \left[ r ^ {n} \left(A _ {n} ^ {(2)} \sin n \theta + B _ {n} ^ {(2)} \cos n \theta\right) + r ^ {- n} \left(C _ {n} ^ {(2)} \sin n \theta + D _ {n} ^ {(2)} \cos n \theta\right) \right]
$$

(3) 确定常数

$\textcircled{1}$ 因为有外加均匀场，它们对x轴对称，可考虑 $\varphi _ { 1 }$ 、 $\varphi _ { 2 }$ 也相对x轴对称（ $\varphi ( \theta )$ 为偶函数），所以 $\varphi _ { 1 } ~ \varphi _ { 2 }$ 中不应包含 项，故： $A _ { n } ^ { ( 1 ) } , A _ { n } ^ { ( 2 ) } , C _ { n } ^ { ( 1 ) } , C _ { n } ^ { ( 2 ) }$ Y 均为零。

$\textcircled { 2 } \ r = 0 \ \textcircled { \varphi _ { 1 } = }$ ② $\varphi _ { 1 } =$ 常数（或零），有限，故 $\varphi _ { 1 }$ 中不应有 $r ^ { - n }$ 项 $\Rightarrow D _ { n } ^ { ( 1 ) } \equiv 0$ o $r \to \infty \ \varphi _ { 2 } \to - E _ { 0 } r \cos \theta$ （均匀场电势）

因此 $\varphi _ { 2 }$ 中不含 $r ^ { n }$ 项（ $n \neq 1 )$ ，得 $B _ { 1 } ^ { ( 2 ) } = - E _ { 0 }$ B（2） $B _ { n } ^ { ( 2 ) } \equiv 0$ 

$$
\left\{ \begin{array}{l l} \varphi_ {1} = \sum_ {n = 1} ^ {\infty} B _ {n} ^ {(1)} r ^ {n} \cos n \theta & 0 <   r <   a \\ \varphi_ {2} = - E _ {0} r \cos \theta + \sum_ {n = 1} ^ {\infty} D _ {n} ^ {(2)} r ^ {- n} \cos n \theta & a <   r <   \infty \end{array} \right.
$$

③r=a 时，

$$
\begin{array}{l} \left. \varphi_ {1} \right| _ {r = a} = \left. \varphi_ {2} \right| _ {r = a} \quad \left. \varepsilon \frac {\partial \varphi_ {1}}{\partial r} \right| _ {r = a} = \left. \varepsilon \frac {\partial \varphi_ {2}}{\partial r} \right| _ {r = a} \\ \left\{ \begin{array}{l} \sum_ {n = 1} ^ {\infty} B _ {n} ^ {(1)} a ^ {n} \cos n \theta = - E _ {0} a \cos \theta + \sum_ {n = 1} ^ {\infty} D _ {n} ^ {(2)} a ^ {- n} \cos n \theta \\ \varepsilon \sum_ {n = 1} ^ {\infty} n B _ {n} ^ {(1)} a ^ {n - 1} \cos n \theta = - \varepsilon_ {0} E _ {0} \cos \theta + \varepsilon_ {0} \sum_ {n = 1} ^ {\infty} (- n) D _ {n} ^ {(2)} a ^ {- (n + 1)} \cos n \theta \end{array} \right. \\ \end{array}
$$

两边 为任意值，cos $\theta$ 前系数应相等（ $n = 1 , 2 , \cdots )$ 

$$
\begin{array}{l} \begin{array}{r l} {n = 1} & {\left\{ \begin{array}{l l} B _ {1} ^ {(1)} a = - E _ {0} a + D _ {1} ^ {(2)} a ^ {- 1} \\ \varepsilon B _ {1} ^ {(1)} = - \varepsilon_ {0} E _ {0} - \varepsilon_ {0} D _ {1} ^ {(2)} a ^ {- 2} \end{array} \right. \Rightarrow \left\{ \begin{array}{l l} D _ {1} ^ {(2)} = \frac {\varepsilon - \varepsilon_ {0}}{\varepsilon + \varepsilon_ {0}} E _ {0} a ^ {2} \\ B _ {1} ^ {(1)} = \frac {- 2 \varepsilon_ {0}}{\varepsilon + \varepsilon_ {0}} E _ {0} \end{array} \right.} \end{array} \\ n \neq 1 (n > 1) \left\{ \begin{array}{l} B _ {n} ^ {(1)} a ^ {n} = D _ {n} ^ {(2)} a ^ {- n} \\ \varepsilon n B _ {n} ^ {(1)} a ^ {n - 1} = - \varepsilon_ {0} n D _ {n} ^ {(2)} a ^ {- (n + 1)} \Rightarrow \left\{ \begin{array}{l} B _ {n} ^ {(1)} = 0 \\ D _ {n} ^ {(2)} = 0 \end{array} \right. (n > 1) \end{array} \right. \\ \end{array}
$$

（4）解为

$$
\left\{ \begin{array}{l} \varphi_ {1} = - \frac {2 \varepsilon_ {0}}{\varepsilon + \varepsilon_ {0}} E _ {0} r \cos \theta \quad 0 <   r <   a \\ \varphi_ {2} = - E _ {0} r \cos \theta + \frac {\varepsilon - \varepsilon_ {0}}{\varepsilon + \varepsilon_ {0}} \frac {a ^ {2}}{r} E _ {0} \cos \theta \quad a <   r <   \infty \end{array} \right.
$$

（5）求柱内电场： $\varphi _ { 1 } = - { \frac { 2 \varepsilon _ { 0 } } { \varepsilon + \varepsilon _ { 0 } } } E _ { 0 } x \qquad ( r \cos \theta = x )$ 280Eox

$$
E _ {1 x} = \frac {2 \varepsilon_ {0}}{\varepsilon + \varepsilon_ {0}} E _ {0} \qquad E _ {1 y} = E _ {1 z} = 0
$$

$$
\vec {E} _ {1} = + \frac {2 \varepsilon_ {0}}{\varepsilon + \varepsilon_ {0}} \vec {E} _ {0} \text {仍 沿} \mathbf {x} \text {方 向}
$$

$$
\because \quad \frac {2 \varepsilon_ {0}}{\varepsilon + \varepsilon_ {0}} <   1 \therefore E _ {1} <   E _ {0}
$$

$$
\overrightarrow {E} _ {P} = \overrightarrow {E} _ {1} - \overrightarrow {E} _ {0} = \frac {\varepsilon_ {0} - \varepsilon}{\varepsilon_ {0} + \varepsilon} \overrightarrow {E} _ {0} = - \frac {\varepsilon - \varepsilon_ {0}}{\varepsilon + \varepsilon_ {0}} \overrightarrow {E} _ {0}
$$

![image](images/174c8e78460fe4e3effd87ebd020c217e7dce6aa9b2d2c527df6c788d0a70847.jpg)


# （6）柱面上束缚面电荷分布

$$
\frac {\boldsymbol {\sigma} + \boldsymbol {\sigma} _ {P}}{\varepsilon_ {0}} = \vec {n} \cdot (\vec {E} _ {2} - \vec {E} _ {1}) \quad \boldsymbol {\sigma} = 0
$$

$$
\sigma_ {P} = \varepsilon_ {0} (E _ {2 n} - E _ {1 n}) = \varepsilon_ {0} (- \frac {\partial \varphi_ {2}}{\partial r} + \frac {\partial \varphi_ {1}}{\partial r}) _ {r = a}
$$

$$
\begin{array}{l} = \varepsilon_ {0} [ E _ {0} \cos \theta + \frac {\varepsilon - \varepsilon_ {0}}{\varepsilon + \varepsilon_ {0}} E _ {0} \cos \theta - \frac {2 \varepsilon_ {0}}{\varepsilon + \varepsilon_ {0}} E _ {0} \cos \theta ] \\ = \frac {2 \varepsilon_ {0} (\varepsilon - \varepsilon_ {0})}{\varepsilon + \varepsilon_ {0}} E _ {0} \cos \theta \\ \end{array}
$$

（7）若圆柱为导体，可用上述方法重新求解，或令

$$
\left\{ \begin{array}{l} \varphi_ {1} = 0 \\ \varphi_ {2} = - E _ {0} r \cos \theta + \frac {a ^ {2}}{r} E _ {0} \cos \theta \\ \sigma = 2 \varepsilon_ {0} E _ {0} \cos \theta \end{array} \right.
$$

# 3.6.3 球坐标系中的分离变量法

$$
\frac {1}{r ^ {2}} \frac {\partial}{\partial r} \left(r ^ {2} \frac {\partial \varphi}{\partial r}\right) + \frac {1}{r ^ {2} \sin \theta} \frac {\partial}{\partial \theta} \left(\sin \theta \frac {\partial \varphi}{\partial \theta}\right) + \overbrace {r ^ {2} \sin^ {2} \theta} ^ {1} \frac {\partial^ {2} \varphi}{\partial \phi^ {2}} = 0
$$

$$
\frac {1}{r ^ {2}} \frac {\partial}{\partial r} (r ^ {2} \frac {\partial \varphi}{\partial r}) + \frac {1}{r ^ {2} \sin \theta} \frac {\partial}{\partial \theta} (\sin \theta \frac {\partial \varphi}{\partial \theta}) = 0 \quad \varphi = f (r) g (\theta)
$$

$$
\frac {g (\theta)}{r ^ {2}} \frac {\partial}{\partial r} \left[ r ^ {2} \frac {\partial f (r)}{\partial r} \right] + \frac {f (r)}{r ^ {2} \sin \theta} \frac {\partial}{\partial \theta} \left[ \sin \theta \frac {\partial g (\theta)}{\partial \theta} \right] = 0 \Longleftrightarrow \frac {r ^ {2}}{f (r) g (\theta)}
$$

$$
\frac {1}{f (r)} \frac {\partial}{\partial r} \left[ r ^ {2} \frac {\partial f (r)}{\partial r} \right] + \frac {1}{g (\theta) \sin \theta} \frac {\partial}{\partial \theta} \left[ \sin \theta \frac {\partial g (\theta)}{\partial \theta} \right] = 0
$$

$$
m (m + 1)
$$

$$
\frac {d}{d r} \left(r ^ {2} \frac {d f (r)}{d r}\right) - m (m + 1) f (r) = 0
$$

$$
- m (m + 1)
$$

欧拉型方程

$$
f (r) = A _ {m} r ^ {m} + B _ {m} r ^ {- (m + 1)}
$$

$$
\frac {1}{\sin \theta} \frac {d}{d \theta} \left(\sin \theta \frac {d g (\theta)}{d \theta}\right) + m (m + 1) g (\theta) = 0
$$

引入新的自变量x令 x =cos0

$$
\frac {d}{d \theta} = \frac {d}{d x} \frac {d x}{d \theta} = - \sin \theta \frac {d}{d x}
$$

$$
\frac {d}{d x} \left[ \left(1 - x ^ {2}\right) \frac {d g (x)}{d x} \right] + \lambda g (x) = 0
$$

注意：x只是一个记号，并不是直角坐标系中的x。

勒让德方程

研究 $0 \leq \theta \leq \pi$ 即-1≤x≤1

则此时的勒让德方程只有一个有界解，它为m阶多项式，记作$\mathrm { P } _ { m } \left( x \right)$ 

当m为偶数时， $P _ { m } ( x )$ 只有偶次项，当为奇数时，则只有奇数项。

![image](images/ddfdee2cc5bd5d611eda6eb9dc05dcb4dbc28811bf0f357c63dc0a88897f9b04.jpg)


$$
\begin{array}{r l} & \mathrm {P} _ {0} (x) = 1 \\ & \mathrm {P} _ {1} (x) = x = \cos \theta \\ & \mathrm {P} _ {2} (x) = \frac {1}{2} (3 x ^ {2} - 1) = \frac {1}{2} (3 \cos^ {2} \theta - 1) \\ & \mathrm {P} _ {3} (x) = \frac {1}{2} (5 x ^ {2} - 3 x) = \frac {1}{2} (5 \cos^ {3} \theta - 3 \cos \theta) \\ & \mathrm {P} _ {4} (x) = \frac {1}{8} (3 5 x ^ {4} - 3 0 x ^ {2} + 3) \\ & = \frac {1}{8} (3 5 \cos^ {4} \theta - 3 0 \cos^ {2} \theta + 3) \\ & \mathrm {P} _ {5} (x) = \frac {1}{8} (6 3 x ^ {5} + 7 0 x ^ {3} + 1 5 x) \\ & = \frac {1}{8} (6 3 \cos^ {5} \theta - 7 0 \cos^ {3} \theta + 1 5 \cos \theta) \end{array}
$$

# 让德多项

对于任意m， $P _ { m } ( x )$ 可用下式计算：

勒让德多项式具有正交性： $\mathrm { P } _ { m } ( x ) = \frac { 1 } { 2 ^ { m } m ! } \frac { d ^ { m } } { d x ^ { m } } ( x ^ { 2 } - 1 ) ^ { m }$ 

$$
\int_ {0} ^ {\pi} \mathrm {P} _ {m} (\cos \theta) \mathrm {P} _ {n} (\cos \theta) \sin \theta d \theta = \int_ {- 1} ^ {1} \mathrm {P} _ {m} (x) \mathrm {P} _ {n} (x) d x = 0
$$

$$
\int_ {0} ^ {\pi} \left[ \mathrm {P} _ {m} (\cos \theta) \right] ^ {2} \sin \theta d \theta = \int_ {- 1} ^ {1} \left[ \mathrm {P} _ {m} (x) \right] ^ {2} d x = \frac {2}{2 m + 1}
$$

球面坐标系中的电位解为：

$$
\varphi (r, \theta) = \sum_ {m = 0} ^ {\infty} \left(A _ {m} r ^ {m} + B _ {m} r ^ {- (m + 1)}\right) P _ {m} (\cos \theta)
$$

![image](images/94e42935cc46f6b56daf72d65ea84c20734003e21a555523c1bd8aba8e4fe36d.jpg)


# 例 3.6.3 设半径为 $a$ ，介电常数为 的介质球放在无限大的真

空中，受到均匀电场 $E _ { 0 }$ 的作用，如图所示。试求介质球内的电场强度。

解 取球坐标系， 令 $E _ { 0 }$ 的方向与 $Z$ 轴一致，即 $\vec { E } _ { 0 } = \vec { e } _ { z } E _ { 0 }$ 。 显然，此时场分布以 $Z$ 轴为旋转对称，因此与 $\phi$ 无关。这样，球内外的电位分布函数可取为

![image](images/d29c10198d1c8ed5ed41dd8830e56c6e8ebd80bf6d2bcc659511e7b6d5efc8e8.jpg)


$$
\phi (r, \theta) = \sum_ {n = 0} ^ {\infty} \left(C _ {n} r ^ {n} + D _ {n} r ^ {- (n + 1)}\right) P _ {n} (\cos \theta)
$$

则球内外电位分别为

$$
\phi_ {i} (r, \theta) = \sum_ {n = 0} ^ {\infty} C _ {n} r ^ {n} \mathrm {P} _ {n} (\cos \theta) + \sum_ {n = 0} ^ {\infty} D _ {n} r ^ {- (n + 1)} \mathrm {P} _ {n} (\cos \theta) \qquad (r <   a)
$$

$$
\phi_ {o} (r, \theta) = \sum_ {n = 0} ^ {\infty} A _ {n} r ^ {n} \mathrm {P} _ {n} (\cos \theta) + \sum_ {n = 0} ^ {\infty} B _ {n} r ^ {- (n + 1)} \mathrm {P} _ {n} (\cos \theta) \quad (r > a)
$$

# 球内外电位函数应该满足下列边界条件：

$\textcircled{1}$ 球心电位 $\varphi _ { \mathrm { i } } ( 0 , \theta )$ 应为有限值；

$\textcircled{2}$ 无限远处电场未受干扰，因此电位应为

$$
\varphi_ {\mathrm {o}} (\infty , \theta) = - E _ {0} r \cos \theta = - E _ {0} r P _ {1} (\cos \theta)
$$

$\textcircled{3}$ 球内电位与球外电位在球面上应该连续，即

$$
\varphi_ {\mathrm {i}} (a, \theta) = \varphi_ {\mathrm {o}} (a, \theta)
$$

$\textcircled{4}$ 根据边界上电位移法向分量的连续性，获知球面上内外电位的法向导数应满足

$$
\varepsilon \frac {\partial \phi_ {\mathrm {i}}}{\partial r} \bigg | _ {r = a} = \varepsilon_ {0} \frac {\partial \phi_ {\mathrm {o}}}{\partial r} \bigg | _ {r = a}
$$

考虑到边界条件 $\textcircled{1}$ ，系数 $\underset { \infty } { \cal D } { } _ { n }$ 应为零，即

$$
\phi_ {\mathrm {i}} (r, \theta) = \sum_ {n = 0} C _ {n} r ^ {n} P _ {n} (\cos \theta)
$$

为了满足边界条件 $\textcircled{2}$ ，除了 $\textstyle { \mathcal { A } } _ { 1 }$ 以外的系数 $A _ { n } = \mathbf { 0 }$ ，且 $A _ { 1 } = - E _ { 0 }$ ，即

$$
\phi_ {\mathrm {o}} (r, \theta) = - E _ {0} r P _ {1} (\cos \theta) + \sum_ {n = 0} ^ {\infty} B _ {n} r ^ {- (n + 1)} P _ {n} (\cos \theta)
$$

再考虑到边界条件 $\textcircled{3}$ ，得

$$
\sum_ {n = 0} ^ {\infty} C _ {n} a ^ {n} P _ {n} (\cos \theta) = - E _ {0} a P _ {1} (\cos \theta) + \sum_ {n = 0} ^ {\infty} B _ {n} a ^ {- (n + 1)} P _ {n} (\cos \theta)
$$

为了进一步满足边界条件 $\textcircled{4}$ ，得

$$
\sum_ {n = 0} ^ {\infty} \varepsilon_ {r} n C _ {n} a ^ {n - 1} P _ {n} (\cos \theta) = - E _ {0} P _ {1} (\cos \theta) - \sum_ {n = 0} ^ {\infty} (n + 1) B _ {n} a ^ {- (n + 2)} P _ {n} (\cos \theta)
$$

式中 $\varepsilon _ { r } = \varepsilon / \varepsilon _ { 0 }$ 

由于上两式对于所有的 $\theta$ 值均应满足，因此等式两边对应的各项系数应该相等。由此获知各系数分别为

$$
B _ {0} = C _ {0} = 0 B _ {1} = E _ {0} a ^ {3} \left(\frac {\varepsilon_ {r} - 1}{\varepsilon_ {r} + 2}\right)
$$

$$
C _ {1} = - \frac {3 E _ {0}}{\varepsilon_ {r} + 2} \quad B _ {n} = C _ {n} = 0, \quad (n \geq 2)
$$

代入前式，求得球内外电位分别为

$$
\phi_ {\mathrm {i}} (r, \theta) = - \frac {3 E _ {0}}{\varepsilon_ {r} + 2} r \cos \theta = - \frac {3 E _ {0}}{\varepsilon_ {r} + 2} z
$$

$$
\phi_ {\mathrm {o}} (r, \theta) = - E _ {0} r \cos \theta + \frac {\varepsilon_ {r} - 1}{\varepsilon_ {r} + 2} \frac {E _ {0} a ^ {3}}{r ^ {2}} \cos \theta
$$

值得注意的是球内的电场分布。已知 $\vec { E } = - \nabla \varphi ,$ ，求得球内的电场为

$$
\boldsymbol {E} _ {\mathrm {i}} = - \frac {\partial \varphi_ {\mathrm {i}}}{\partial z} = \frac {3 E _ {0} \varepsilon_ {0}}{\varepsilon + 2 \varepsilon_ {0}} = \frac {3 E _ {0}}{\varepsilon_ {r} + 2} <   E _ {0}
$$

可见，球内电场仍然为均匀电场，而且球内场强低于球外场强。

球内外的电场线如图示。

如果在无限大的介电常数为 $\varepsilon$ 的均匀介质中存在球形气泡，那么当外加均匀电场时，气泡内的电场强度应为

$$
\boldsymbol {E} _ {i} = \frac {3 \varepsilon E _ {0}}{\varepsilon_ {0} + 2 \varepsilon} = \frac {3 \varepsilon_ {r} E _ {0}}{1 + 2 \varepsilon_ {r}} > E _ {0}
$$

那么，泡内的场强高于泡外的场强。

![image](images/1d6391629a22b9599c6df0616f615e4cdad980a6251c2b752811ae24f55cc6eb.jpg)
