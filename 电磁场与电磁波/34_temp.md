# 3.4 静态场的边值问题及解的惟一性定理

静态场问题：分布型问题和边值型问题

边值问题分类：解析法（镜像法和分离变量法）数值法（有限差分法）

边值问题定义：在给定的边界条件下，求解位函数的泊松方程或拉普拉斯方程

# 3.4.1 边值问题的类型

中 第一类边值问题（或狄里赫利问题）

已知场域边界面上的位函数值，即

$$
\varphi \mid_ {S} = f _ {1} (S)
$$

第二类边值问题 （或纽曼问题）

已知场域边界面上的位函数的法向导数值，即

![image](images/dd63e147ce9a66eaf8c2ee6ad68dbe7e4a9c7e156307972065831c13a5593d9f.jpg)


$$
\frac {\partial \varphi}{\partial n} | _ {S} = f _ {2} (S)
$$

第三类边值问题（或混合边值问题）

已知场域一部分边界面上的位函数值，而另一部分边界面上则已知位函数的法向导数值，即 $\varphi | _ { S _ { 1 } } = f _ { 1 } ( S _ { 1 } ) \setminus \frac { \partial \varphi } { \partial n } | _ { S _ { 2 } } = f _ { 2 } ( S _ { 2 } )$ 

周期边界条件

$$
\varphi \big | _ {\phi} = \varphi \big | _ {(\phi + 2 \pi)}
$$

![image](images/74c6ee9712c78533dbb67ad95d102832a9a8827e1ba05d16ef756b0b236b1f58.jpg)


中 自然边界条件 （无界空间）

$\operatorname* { l i m } _ { r \to \infty } r \varphi =$ 有限值

![image](images/2a8ccfef9c9f86871c62b48b9d51d7e41690edeebaa70b8ba19165b259e516e0.jpg)


衔接条件 （连续性条件）

不同媒质分界面上的边界条件，如

$$
\varphi_ {1} = \varphi_ {2}, \varepsilon_ {1} \frac {\partial \varphi_ {1}}{\partial n} = \varepsilon_ {2} \frac {\partial \varphi_ {2}}{\partial n}
$$

![image](images/3c27bae33eff491321bfb33c8ee4c54fe8108f1159a83d203724b756a9e7a89d.jpg)


例：

![image](images/a8399882bb3b8f4fbe3de1788e89bfd289754ddc9c3f0e71ed945f9a56ab16c2.jpg)


$$
\frac {\partial^ {2} \varphi}{\partial x ^ {2}} + \frac {\partial^ {2} \varphi}{\partial y ^ {2}} = 0
$$

$$
\varphi (0, y) = 0, \varphi (a, y) = 0
$$

$$
\varphi (x, 0) = 0, \varphi (x, b) = U _ {0}
$$

# （第一类边值问题）

例：

![image](images/f893d61d87069027a6cfb93d602943dd76f29952f554aff187ecea5293fca095.jpg)


$$
\frac {\partial^ {2} \varphi}{\partial x ^ {2}} + \frac {\partial^ {2} \varphi}{\partial y ^ {2}} = 0
$$

$$
\left. \frac {\partial \varphi}{\partial x} \right| _ {x = 0} = 0, \left. \frac {\partial \varphi}{\partial x} \right| _ {x = a} = 0
$$

$$
\varphi (x, 0) = 0, \varphi (x, b) = U _ {0}
$$

# （第三类边值问题）

# 3.4.2 静电场的惟一性定理

惟一性定理的表述

在场域V 的边界面S上给定 $\varphi$ 或 n 的值，则泊松方程或拉普拉斯方程在场域V具有惟一解。

![image](images/414182444f6a19a13acdf64a07411f51274d220d24afc96651eeaee582e01418.jpg)


惟一性定理的重要意义

给出了静态场边值问题具有惟一解的条件

为静态场边值问题的各种求解方法提供了理论依据

为求解结果的正确性提供了判据

惟一性定理的证明 （以静电场为例）

反证法：假设解不惟一，则有两个位函数 $\varphi _ { 1 }$ 和 $\varphi _ { 2 }$ 在场域V内满足同样的方程，即

$$
\nabla^ {2} \varphi_ {1} = f, \qquad \nabla^ {2} \varphi_ {2} = f
$$

且在边界面S 上满足同样的边界条件。

令 $\varphi _ { 0 } = \varphi _ { 1 } - \varphi _ { 2 }$ 则在场域V内

$$
\nabla^ {2} \varphi_ {0} = \nabla^ {2} \varphi_ {1} - \nabla^ {2} \varphi_ {2} = f - f = 0
$$

且在边界面S 上有

$\varphi _ { 0 }  _ { s } = \varphi _ { 1 }  _ { s } - \varphi _ { 2 }  _ { s } = 0$ 或

或 $\varphi _ { 0 } | _ { S _ { 1 } } = \varphi _ { 1 } | _ { S _ { 1 } } - \varphi _ { 2 } | _ { S _ { 1 } } = 0 ,$ 2 2|s=0

![image](images/e0a7cfa592da2fb8279a73589560a4fcc9e444a2ccc7201796b64be4485a7747.jpg)


# 由格林第一恒等式

$$
\int_ {V} \left(\psi \nabla^ {2} \varphi + \nabla \psi \cdot \nabla \varphi\right) \mathrm {d} V = \oint_ {S} \psi \frac {\partial \varphi}{\partial n} \mathrm {d} S
$$

可得到 $\int _ { \cal { V } } \left( { \nabla } \varphi _ { \mathrm { { 0 } } } \right) ^ { 2 } \mathrm { d } V = \oint _ { \cal { S } } \varphi _ { \mathrm { { 0 } } } \frac { \partial \varphi _ { \mathrm { { 0 } } } } { \partial n } \mathrm { d } S = 0$ φods =0

$$
\Longrightarrow (\nabla \varphi_ {0}) ^ {2} = 0 \Longrightarrow \nabla \varphi_ {0} = 0 \Longrightarrow \varphi_ {0} = C
$$

![image](images/77ec46134ad22d1c45d55f500d9b0e44a5555a44d707a27da2dafd492864f4a3.jpg)


对于第一类边界条件： $\varphi _ { 0 } \big | _ { S } = 0$ C = 0  1 2

对于第二类边界条件：若 $\varphi _ { 1 }$ 和 $\varphi _ { 2 }$ 取同一点Q为参考点 ，则

$$
\varphi_ {0} \Big | _ {Q} = 0 \quad \Longrightarrow \quad C = 0 \quad \Longrightarrow \quad \varphi_ {1} = \varphi_ {2}
$$

对于第三类边界条件： $\varphi _ { 0 } \big | _ { S _ { 1 } } = 0 \longmapsto C = 0 \longmapsto \varphi _ { 1 } = \varphi _ { 2 }$ 

![image](images/97872c64a95285228c2d35c41362143cc9f35eb3baa013a1315db0f91e2f86bd.jpg)


