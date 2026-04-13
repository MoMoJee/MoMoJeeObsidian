# 3.5 镜像法求解高维问题

# ❖ 问题的提出

当有电荷（这里称为原点荷）存在于导体表面附近时，导体表面会出现感应电荷，而感应电荷将影响场的分布。

# 几个实例

中 接地导体板附近有一个点电荷，如图所示。

非均匀感应电荷

等效电荷

非均匀感应电荷产生的电位很难求解，可以用等效电荷的电位替代

接地导体球附近有一个点电荷，如图。

![image](images/83cd42c9adcd57073610a5bc861e6217a784c19cd8f3a5b3848ac747f9a5fe5b.jpg)


中 接地导体柱附近有一个同轴的线电荷分布，情况与上面平板或球的类似，但等效电荷为线电荷。

结论：所谓镜像法是将不均匀电荷分布的作用等效为点电荷或线电荷的作用。

问题：这种等效电荷是否存在？ 这种等效是否合理？

# 镜像法的基本思想

用位于场域边界外虚设的较简单的镜像电荷分布来等效替代该边界上未知的较为复杂的电荷分布，从而可以将原含该边界的非均匀媒质空间变换成无限大单一均匀媒质的空间，使分析计算过程得以明显简化的一种间接求解法。

# 镜像法的理论基础— 解的惟一性定理

在导体形状、几何尺寸、带电状况和媒质几何结构、特性不变的前提条件下，根据惟一性定理，只要找出的解答满足在同一泛定方程下问题所给定的边界条件，那就是该问题的解答，并且是惟一的解答。镜像法正是巧妙地应用了这一基本原理、面向多种典型结构的工程电磁场问题所构成的一种有效的解析求解法。

# 镜像法应用的关键点

中 镜像电荷的确定

镜像电荷的个数、位置及其电量大小— “三要素” ；

中 等效求解的 “有效场域” 确定

# 确定镜像电荷的两条原则

中 镜像电荷必须位于所求解的场区域以外的空间中；

中 镜像电荷的个数、位置及电荷量的大小以满足所求解的场区域的边界条件为基本准则来进行确定。

不同介质分界面问题 恒定磁场问题

# 3.5.1 接地导体平面的镜像

# 1. 点电荷对无限大接地导体平面的镜像

![image](images/2b29494ecb48db4917b690505cef6536d3b749fbd01ae9d3b1b10eb480d6bcc2.jpg)


方程： $\nabla ^ { 2 } \varphi = - \frac { q } { \varepsilon } \delta \big ( x , y , z - h \big ) , z > 0$ 

边界条件

$$
\varphi \mid_ {z = 0} = 0
$$

# 3.5.1 接地导体平面的镜像

# 1. 点电荷对无限大接地导体平面的镜像

![image](images/7f7bac06d59f7e2e5c7c83be9a5379a7ac3370f0918c9e456cc7bccd4d3515b8.jpg)


镜像电

电位函数 $\psi - \overline { { { 4 \pi \varepsilon } } } ^ { \mathrm { ( } } \overline { { { R } } } ^ { \mathrm { - } } \overline { { { R ^ { \prime } } } } ^ { \mathrm { ) } } \quad \setminus \varepsilon \mathrm { \subset U } ^ { \mathrm { } }$ 

因 $z = 0$ 时， $\begin{array} { r l } { R = R ^ { \prime } } & { { } \varphi \big | _ { z = 0 } = 0 } \end{array}$ 

满足原问题的边界条件，所得的结果是正确的。

上半空间( z≥0 ） 的电位函数

$$
\varphi (x, y, z) = \frac {q}{4 \pi \varepsilon} [ \frac {1}{\sqrt {x ^ {2} + y ^ {2} + (z - h) ^ {2}}} - \frac {1}{\sqrt {x ^ {2} + y ^ {2} + (z + h) ^ {2}}} ] \quad (z \geq 0)
$$

导体平面上的感应电荷面密度为

$$
\rho_ {S} = - \varepsilon \frac {\partial \varphi}{\partial z} \bigg | _ {z = 0} = - \frac {q h}{2 \pi (x ^ {2} + y ^ {2} + h ^ {2}) ^ {3 / 2}}
$$

![image](images/a35fec6b3a019cbbc2887ae333ba5afaa7d12cbe1ed22e392e7beea15232f858.jpg)


导体平面上的总感应电荷为

$$
\begin{array}{l} q _ {i n} = \int_ {S} \rho_ {S} \mathrm {d} S = - \frac {q h}{2 \pi} \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} \frac {\mathrm {d} x \mathrm {d} y}{\left(x ^ {2} + y ^ {2} + h ^ {2}\right) ^ {3 / 2}} \\ = - \frac {q h}{2 \pi} \int_ {0} ^ {2 \pi} \int_ {0} ^ {\infty} \frac {\rho \mathrm {d} \rho \mathrm {d} \phi}{\left(\rho^ {2} + h ^ {2}\right) ^ {3 / 2}} = - q \\ \end{array}
$$

![image](images/087d44cc5056dc879ded574834dcac1e0e9f3c448fb00d6f297465f78a8555e2.jpg)


![image](images/0b28667e5712fd6d6ee7e7a04bcdbe809de24144ec84682993df2b47a695218b.jpg)


![image](images/cc4db1d5d948dab8560f3766816d5409ef51ef7efda171e065273bddd3c661aa.jpg)



(d）两个等值异号电荷


2.线电荷对无限大接地导体平面的镜像原问题

方程 $\nabla ^ { 2 } \varphi = - \frac { \rho _ { l } } { \varepsilon } \delta \big ( x , z - h \big ) , z > 0 ;$ 

边界条件φ =0Iz=0

![image](images/755a158d5785c60cb816788dd729f1c4a3eabf4d994a608bf6399b4ebb00c57d.jpg)


![image](images/5bbdf7593c44b2920f83a30f3ded512f6913d84626df75f353622f1c982bc8ef.jpg)


# 2. 线电荷对无限大接地导体平面的镜像

镜像线电荷： $\rho _ { l } ^ { \prime } = - \rho _ { l } , z ^ { \prime } = - h$ 

电位函数 $\varphi = \frac { \rho _ { l } } { 2 \pi \varepsilon } \ln \frac { R ^ { \prime } } { R } \quad ( z \geq 0 )$ Pln

当z=0时， $R ^ { \prime } = R \enspace \longrightarrow \enspace \varphi = 0$ 

![image](images/d31cafdb1408e198d7252c41120be18f6f7774f04308b71b1b2a844fb848aef4.jpg)


满足原问题的边界条件，所得的解是正确的。

# 3. 点电荷对相交半无限大接地导体平面的镜像

如图所示，两个相互垂直相连的半无限大接地导体平板，点电荷q 位于(d1, ${ \bf d } _ { 2 }$ )处。

方程： $\nabla ^ { 2 } \varphi = - \frac { q } { \varepsilon } \delta \big ( x - d _ { 1 } , y - d _ { 2 } , z \big ) , ( x > 0 , y > 0 )$ 

边界条件 $\varphi \big | _ { x = 0 } = 0$ 

$$
\varphi \left| _ {y = 0} \right. = 0
$$

$$
\varphi \left| _ {\sqrt {x ^ {2} + y ^ {2} + z ^ {2}} \rightarrow \infty} = 0 \right.
$$

![image](images/9234a9d729d733a04d110082f663a76a4e583d8f8184b3cfead50365f44e2998.jpg)


# 3. 点电荷对相交半无限大接地导体平面的镜像

对于平面1，有镜像电荷q1=－q，对于平面2，有镜像电荷 $q _ { 2 } { = } - \mathbf { q }$ d1, d2 )，位于 $( d _ { 1 } , \ : - d _ { 2 } )$ 

显然， $\pmb q _ { 1 }$ 对平面 2 以及 $\pmb { q } _ { 2 }$ 对平面 1 均不能满足边界条件。

只有在 $( - d _ { 1 } , \textrm { -- } d _ { 2 } )$ 处再设置一镜像电荷 $q _ { 3 } = q$ ，所有边界条件才能得到满足。

$\varphi = \frac { q } { 4 \pi \varepsilon } ( \frac { 1 } { R } - \frac { 1 } { R _ { 1 } } - \frac { 1 } { R _ { 2 } } + \frac { 1 } { R _ { 3 } } )$ 1电位函数

![image](images/39b0d05e73c62859b38590e789305156058b964dbe3b83cc76a6f24e855e5308.jpg)


![image](images/15b332c40cc4a1a645f4efe17cc757b3d2843aaad4c879c142776a42e8d101cc.jpg)


如果两导体平面不是相互垂直，而是相

交成 $a$ 角，只要 $\dot { \alpha } = \frac { \pi } { n }$ ，这里的n为整数，就

能用镜像法求解，其镜像电荷数为有限的 $( 2 n - 1 )$ 个。

（第六版）3.5节习题1： 一个点电荷q与无限大的接地导体平面距离为d，如果把它移至无穷远处，需要做多少功？

解：移动电荷q时，外力需要克服电场力做功，而电荷q受的电场力来源于导体板上的感应电荷。可以求电荷q 移至无穷远

时电场力所做的功。

由镜像法， 感应电荷的电场可以用像电荷 $q ^ { \prime } { = } { - } q$ 替代。当电荷q 移至x时，像电荷 $\pmb q$ '应位于－x，则有

$$
\vec {E} ^ {\prime} (x) = \vec {\pmb {e}} _ {x} \frac {- q}{4 \pi \varepsilon_ {0} (2 x) ^ {2}}
$$

$$
\begin{array}{l} \rightarrow W _ {e} = \int_ {d} ^ {\infty} q \vec {E} ^ {\prime} (x) \cdot \mathrm {d} \vec {x} = \frac {- q ^ {2}}{4 \pi \varepsilon_ {0}} \int_ {d} ^ {\infty} \frac {1}{(2 x) ^ {2}} \mathrm {d} x = - \frac {q ^ {2}}{1 6 \pi \varepsilon_ {0} d} \\ \longrightarrow W _ {o} = - W _ {e} = \frac {q ^ {2}}{1 6 \pi \varepsilon_ {0} d} \\ \end{array}
$$

![image](images/c323dfadce26571372930491ba7d544a2966894603a30771dac0eae4119347a1.jpg)


# 3.5.2 导体球面的镜像

点电荷对接地导体球面的镜像如图所示，点电荷q 位于半径为a 的接地导体球外，距球心为d 求电势

方程 $\nabla ^ { 2 } \varphi = - \frac { q } { \varepsilon } \delta \left( r - d , \theta , \phi \right)$ 

边界条件φ丨a $\varphi \bigm | _ { r = a } = 0$ 

$$
\varphi \left. \right.\left. \right\rVert_ {r \rightarrow \infty} = 0
$$

![image](images/7767f9cbe7f0f89815f56e5f1bcf0519bc9092bf67ffb652c11af902c1c94991.jpg)


![image](images/3f37af0ead5386c874e413a42c3c739ef2409985d32d5c5b0c342219aa79429c.jpg)


球面上的感应电荷可用镜像电荷q'来等效。q'应位于导体球内（显然不影响原方程），且在点电荷q与球心的连线上，距球心为d'。则有

$$
\varphi = \frac {1}{4 \pi \varepsilon} \left(\frac {q}{R} + \frac {q ^ {\prime}}{R ^ {\prime}}\right)
$$

问题： $d ^ { \prime } = ? q ^ { \prime } = ?$ 

方法：利用导体球面上电位为零确定 $d ^ { \prime }$ 和 ${ \pmb q } ^ { \prime }$ 。

![image](images/176ac7a019e33371e44cff825969796d1cc43ca6862cd249e1e02b94e08f447b.jpg)


![image](images/8cd5f9a8d4c1905bea90cb8755139fc61e688bd6a9f0277f1e7cfcf768f98b5b.jpg)


![image](images/ca508a8ebd75f31e9a9fe7a9a1a0b372da4addc4ac9dbb7ac89e500dfbb90f1a.jpg)


$$
\varphi = \frac {1}{4 \pi \varepsilon} \left[ \frac {q}{\sqrt {r ^ {2} + d ^ {2} - 2 r d \cos \theta}} + \frac {q ^ {\prime}}{\sqrt {r ^ {2} + d ^ {\prime 2} - 2 r d ^ {\prime} \cos \theta}} \right]
$$

由于导体球接地,在球面 $r = a$ 处， $\varphi = 0$ 。于是有

$$
\frac {1}{4 \pi \varepsilon} \left[ \frac {q}{\sqrt {a ^ {2} + d ^ {2} - 2 a d \cos \theta}} + \frac {q ^ {\prime}}{\sqrt {a ^ {2} + d ^ {\prime 2} - 2 a d ^ {\prime} \cos \theta}} \right] = 0
$$

由此得

$$
(a ^ {2} + d ^ {2}) q ^ {\prime 2} - (a ^ {2} + d ^ {\prime 2}) q ^ {2} - 2 a \cos \theta \left(d q ^ {\prime 2} - d ^ {\prime} q ^ {2}\right) = 0
$$

![image](images/8d315221d0d2c4a5a30e07b1b6a73631e31de3a6ae2920d982a8d69de0e79665.jpg)


![image](images/dddc8b5049a6ef3cb45a4dd8f430d591eb551209098e3c9e5b8d005d95cb1efd.jpg)


因上式对任意的 $\theta$ 都成立，所以

$$
\left\{ \begin{array}{l} (a ^ {2} + d ^ {2}) q ^ {\prime 2} - (a ^ {2} + d ^ {\prime 2}) q ^ {2} = 0 \\ d q ^ {\prime 2} - d ^ {\prime} q ^ {2} = 0 \end{array} \right.
$$

由此解得

$$
q ^ {\prime} = - \frac {a}{d} q, \quad d ^ {\prime} = \frac {a ^ {2}}{d} \tag {3.5.6}
$$

和

$q ^ { ' } = - \ q$ $\ d ^ { \prime } = d$ (无意义，舍去)

![image](images/84c58791b7d6dde9eafe1bffa32bebfe451add59c72692b4c0facdbb8abe806c.jpg)


令r＝a， 由球面上电位为零，即 ${ \boldsymbol { \varphi } } = \mathbf { 0 }$ ，得

$$
\frac {q}{R} + \frac {q ^ {\prime}}{R ^ {\prime}} = 0 \rightarrow \frac {R ^ {\prime}}{R} = - \frac {q ^ {\prime}}{q} = \text {常 数}
$$

此式应在整个球面上都成立。

![image](images/0ca417e30687c713dad3d7d6a5010b7be3e503246021d74e2c4c3556dbf220d5.jpg)


条件：若 $\Delta o q P \sim \Delta o P q ^ { \prime }  \frac { R ^ { \prime } } { R } = \frac { d ^ { \prime } } { a } = \frac { a } { d } =$ d'==常数

$$
\Rightarrow d ^ {\prime} = \frac {a ^ {2}}{d} \leftarrow \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \tag {像电荷的位置}
$$

$$
\frac {q ^ {\prime}}{R ^ {\prime}} + \frac {q}{R} = 0 \Rightarrow q ^ {\prime} = - \frac {R ^ {\prime}}{R} q = - \frac {a}{d} q \quad \text {像 电 荷 的 电 量}
$$

$$
\frac {a}{d} <   1 \longrightarrow | q ^ {\prime} | <   | q |
$$

# 球外的电位函数为

$$
\varphi = \frac {q}{4 \pi \varepsilon} \left[ \frac {1}{\sqrt {r ^ {2} + d ^ {2} - 2 r d \cos \theta}} - \frac {a}{d \sqrt {r ^ {2} + (a ^ {2} / d) ^ {2} - 2 r (a ^ {2} / d) \cos \theta}} \right] \quad (r \geq a)
$$

球面上的感应电荷面密度为

$$
\rho_ {S} = - \varepsilon \frac {\partial \varphi}{\partial r} \bigg | _ {r = a} = - \frac {q (d ^ {2} - a ^ {2})}{4 \pi a (a ^ {2} + d ^ {2} - 2 a d \cos \theta) ^ {3 / 2}}
$$

导体球面上的总感应电荷为

$$
q _ {i n} = \int_ {S} \rho_ {S} \mathrm {d} S = - \frac {q (d ^ {2} - a ^ {2})}{4 \pi a} \int_ {0} ^ {2 \pi} \int_ {0} ^ {\pi} \frac {a ^ {2} \sin \theta \mathrm {d} \theta \mathrm {d} \phi}{(a ^ {2} + d ^ {2} - 2 a d \cos \theta) ^ {3 / 2}} = - \frac {a}{d} q
$$

可见，导体球面上的总感应电荷也与所设置的镜像电荷相等。

# 点电荷对接地空心导体球壳的镜像

如图所示接地空心导体球壳的内半径为a ，点电荷q 位于球壳内，与球心相距为 $d ( d < a )$ 。

由于球壳接地， 感应电荷分布在球壳的表面上。 镜像电荷q应放置在导体球壳外，且在点电荷q与球心的连线的延长线上。与点荷位于接地导体球外同样的分析，可得到

$$
q ^ {\prime} = - \frac {a}{d} q, \quad d ^ {\prime} = \frac {a ^ {2}}{d}
$$

![image](images/5ebe4262feafbcca750e88efca6bd946fd096eba84c5b7b4aae4e9a5c240a778.jpg)


中 | q'|>|q|，可见镜像电荷的电荷量大于点电荷的电荷量

# 球壳内的电位

$$
\varphi = \frac {q}{4 \pi \varepsilon_ {0}} \left[ \frac {1}{\sqrt {r ^ {2} + d ^ {2} - 2 r d \cos \theta}} - \frac {a}{d \sqrt {r ^ {2} + (a ^ {2} / d) ^ {2} - 2 r (a ^ {2} / d) \cos \theta}} \right] (r \le a)
$$

感应电荷分布在导体球面的内表面上，电荷面密度为

$$
\rho_ {S} = \varepsilon \frac {\partial \varphi}{\partial r} \bigg | _ {r = a} = - \frac {q (a ^ {2} - d ^ {2})}{4 \pi a (a ^ {2} + d ^ {2} - 2 a d \cos \theta) ^ {3 / 2}}
$$

导体球面的内表面上的总感应电荷为

$$
q _ {i n} = \int_ {S} \rho_ {S} \mathrm {d} S = - \frac {q (a ^ {2} - d ^ {2})}{4 \pi a} \int_ {0} ^ {2 \pi} \int_ {0} ^ {\pi} \frac {a ^ {2} \sin \theta \mathrm {d} \theta \mathrm {d} \phi}{(a ^ {2} + d ^ {2} - 2 a d \cos \theta) ^ {3 / 2}} = - q
$$

可见，在这种情况下，镜像电荷与感应电荷的电荷量不相等。

# 2 点电荷对不接地导体球的镜像

点电荷q 位于一个半径为 $\pmb { a }$ 的不接地导体球外，距球心为d 。 

![image](images/faf6608c3f95831fd197014864978395383981970df16d5ad72816352739abb5.jpg)


导体球不接地时的特点：

❖ 导体球面是电位不为零的等位面

❖球面上既有感应负电荷分布也有感应正电荷分布，但总的感应电荷为零

采用叠加原理来确定镜像电荷

先设想导体球是接地的，则球面上只有总电荷量为q'的感应电荷分布，则

$$
q ^ {\prime} = - \frac {a}{d} q, d ^ {\prime} = \frac {a ^ {2}}{d}
$$

然后断开接地线，并将电荷－q'加于导体球上，从而使总电荷为零。为保持导体球面为等位面，所加的电荷－ $q ^ { \prime }$ 可用一个位于球心的镜像电荷q"来替代，即

$$
\boldsymbol {q} ^ {\prime \prime} = - \boldsymbol {q} ^ {\prime} = \frac {\boldsymbol {a}}{d} \boldsymbol {q}, d ^ {\prime \prime} = \mathbf {0}
$$

球外任意点的电位为

$$
\varphi = \frac {1}{4 \pi \varepsilon_ {0}} \left(\frac {q}{R} + \frac {q ^ {\prime}}{R ^ {\prime}} + \frac {q ^ {\prime \prime}}{r}\right)
$$

![image](images/65e9e4cd1fdada13458437061febe1294cc24acb67d9139a4e960cc0ded794f8.jpg)


# 3.5.2 导体圆柱面的镜像

线电荷对接地导体圆柱面的镜像问题：如图 1 所示，一根电荷线密度为 $\rho _ { l }$ 的无限长线电荷位于半径为 $\pmb { a }$ 的无限长接地导体圆柱面外，与圆柱的轴线平行且到轴线的距离为d。

特点：在导体圆柱面上有感应电荷，圆轴外的电位由线电荷与感应电荷共同产生。 

分析方法：镜像电荷是圆柱面内部与轴线平行的无限长线电荷，如图2所示。

![image](images/53f1380a138f2db7021a6c38f7c06d0f465ddba274ae36efe9c8b9ac65b6a0c1.jpg)



图1 线电荷与导体圆柱


![image](images/173b763b2d15bf32e5c7737d51557e20c432a224a6eb75a2f86853177cd2e776.jpg)



图2 线电荷与导体圆柱的镜像


# 3.5.2 导体圆柱面的镜像

方程 $\nabla ^ { 2 } \varphi = - \frac { \rho _ { l } } { \varepsilon } \delta \big ( \rho - d , \phi \big ) ,$ 

边界条件 $\varphi \mid _ { \rho = a } = 0$ 

![image](images/a519b6516337cdb80294e920c0366edd51cff17e38b537b244f5dcf978fbe6f5.jpg)



图1 线电荷与导体圆柱


![image](images/718b6ffdbd9ff58f8505ea9a7ae5db10f146c2dd9930d7db518f7725c28c141a.jpg)



图2 线电荷与导体圆柱的镜像


例 求长度为2L、电荷线密度为 $\rho _ { l 0 }$ 的均匀带电线的电位。

解 采用圆柱面坐标系，令线电荷与 z 轴相重合，中点位于坐标原点。由于轴对称性，电位与 $\phi$ 无关。

在带电线上位于 $z ^ { \prime }$ 处的线元 $\mathrm { d } l ^ { \prime } = \mathrm { d } z ^ { \prime }$ ，它到点 $P ( \rho , \phi , z )$ 的距离 $R = \sqrt { \rho ^ { 2 } + ( z - z ^ { \prime } ) ^ { 2 } }$ 

则

$$
\begin{array}{l} \varphi (\vec {r} ^ {\prime}) = \frac {\rho_ {l 0}}{4 \pi \varepsilon_ {0}} \int_ {- L} ^ {L} \frac {1}{\sqrt {\rho^ {2} + (z - z ^ {\prime}) ^ {2}}} \mathrm {d} z ^ {\prime} \\ = \frac {\rho_ {l 0}}{4 \pi \varepsilon_ {0}} \ln [ z ^ {\prime} - z + \sqrt {\rho^ {2} + (z - z ^ {\prime}) ^ {2}} ] \Bigg | _ {- L} ^ {L} \\ = \frac {\rho_ {l 0}}{4 \pi \varepsilon_ {0}} \ln \frac {\sqrt {\rho^ {2} + (z - L) ^ {2}} - (z - L)}{\sqrt {\rho^ {2} + (z + L) ^ {2}} - (z + L)} \\ \end{array}
$$

![image](images/a72904aa7ecfadf1e1e386dd3f45413c51936e4c4fdcb5c4ac60d0e0900e721a.jpg)


在上式中若令 ，则可得到无限长直线电荷的电位。当L>>R 时，上式可写为

$$
\varphi (\vec {r}) \approx \frac {\rho_ {l 0}}{4 \pi \varepsilon_ {0}} \ln \frac {\sqrt {\rho^ {2} + L ^ {2}} + L}{\sqrt {\rho^ {2} + L ^ {2}} - L} = \frac {\rho_ {l 0}}{4 \pi \varepsilon_ {0}} \ln \frac {2 L}{\rho^ {2} / 2 L} \approx \frac {\rho_ {l 0}}{2 \pi \varepsilon_ {0}} \ln \frac {2 L}{\rho}
$$

当 $L \to \infty$ 时，上式变为无穷大，这是因为电荷不是分布在有限区域内，而将电位参考点选在无穷远点之故。这时可在上式中加上一个任意常数，则有 $\varphi ( \vec { r } ) = \frac { \rho _ { l 0 } } { 2 \pi \varepsilon _ { 0 } } \ln \frac { 2 L } { \rho } + C$ P

并选择有限远处为电位参考点。例如，选择ρ= a的点为电位参考点，则有$C = - \frac { \rho _ { l 0 } } { 2 \pi \varepsilon _ { 0 } } \ln \frac { 2 L } { a } \qquad \varphi ( \vec { r } ) = \frac { \rho _ { l 0 } } { 2 \pi \varepsilon _ { 0 } } \ln \frac { a } { \rho }$ 2πε。

![image](images/9f588e2da610ed8b0459a27a9dc62305dfa81be70c2968d4d0bbabc8533b111c.jpg)


设镜像电荷的线密度为 $\rho _ { l } ^ { \prime }$ ， 且距圆柱的轴线为 $d ^ { \prime }$ ，则由 $\rho _ { l }$ 和 $\rho _ { l } ^ { \prime }$ 共同产生的电位函数

$$
\varphi = \frac {\rho_ {l}}{2 \pi \varepsilon} \ln \frac {1}{\sqrt {\rho^ {2} + d ^ {2} - 2 \rho d \cos \phi}} + \frac {\rho_ {l} ^ {\prime}}{2 \pi \varepsilon} \ln \frac {1}{\sqrt {\rho^ {2} + d ^ {\prime 2} - 2 \rho d ^ {\prime} \cos \phi}} + C
$$

由于导体圆柱接地，所以当 $\rho = a$ 时，电位应为零，即

$$
\frac {\rho_ {l}}{2 \pi \varepsilon} \ln \frac {1}{a \sqrt {a ^ {2} + d ^ {2} - 2 a d \cos \phi}} + \frac {\rho_ {l} ^ {\prime}}{2 \pi \varepsilon} \ln \frac {1}{\sqrt {a ^ {2} + d ^ {\prime 2} - 2 a d ^ {\prime} \cos \phi}} + C = 0
$$

![image](images/785e18d481f0170bb7d212b748731d1c0f0c1cd891fb43a2bfdf0e6d1c345546.jpg)


![image](images/e962586396452201986fbb6790a7e2642f8dec1e8f52c4d0ba06c6211b15750c.jpg)


$$
\frac {\rho_ {l}}{2 \pi \varepsilon} \ln \frac {1}{a \sqrt {a ^ {2} + d ^ {2} - 2 a d \cos \phi}} + \frac {\rho_ {l} ^ {\prime}}{2 \pi \varepsilon} \ln \frac {1}{\sqrt {a ^ {2} + d ^ {\prime 2} - 2 a d ^ {\prime} \cos \phi}} + C = 0
$$

由于上式对任意的都成立，因此，将上式对φ求导，可以得到

$$
\rho_ {l} d \left(a ^ {2} + d ^ {2}\right) + \rho_ {l} ^ {\prime} d ^ {\prime} \left(a ^ {2} + d ^ {\prime 2}\right) - 2 a d d ^ {\prime} \left(\rho_ {l} + \rho_ {l} ^ {\prime}\right) \cos \phi = 0
$$

所以有 $ \begin{array} { l } { { \rho _ { l } d ( a ^ { 2 } + d ^ { 2 } ) + \rho _ { l } ^ { \prime } d ^ { \prime } ( a ^ { 2 } + d ^ { \prime } { } ^ { 2 } ) = 0 } } \\ { { \rho _ { l } + \rho _ { l } ^ { \prime } = 0 } } \end{array} \} \overset { \rho _ { l } ^ { \prime } = - } { \underset { d ^ { \prime } = \frac { d } { \delta } } { \longrightarrow } } \{ \begin{array} { l l } { { \rho _ { l } ^ { \prime } = - { } \rho _ { l } ^ { \prime } d ^ { \prime } ( a ^ { 2 } + d ^ { \prime } { } ^ { 2 } ) = 0 } } & { { \quad - \{ \begin{array} { l l } { { \rho _ { l } ^ { \prime } = - \rho _ { l } ^ { \prime } d ^ { \prime } ( a ^ { 2 } + d ^ { \prime } { } ^ { 2 } ) = 0 } } & { { \quad - \{ \begin{array} { l l } { { \rho _ { l } ^ { \prime } = - \rho _ { l } ^ { \prime } d ^ { \prime } } } \\ { { d ^ { \prime } = { } \frac { d ^ { \prime } } { d ^ { \prime } } } } } & { { { \quad - \{ \begin{array} { l l } { { d ^ { \prime } } } \end{array} } \} } } \end{array} } } }   \end{array}  \end{array}$ l −d  = ad

导体圆柱面外的电位函数 =PnVd²p²+a²-2pda²cos +C2π d√p²+d²-2pd cosΦ

由 $\rho = a$ 时， ln 2π8 a

故 =Pn√p²+-2pda²cos $\varphi = \frac { \rho _ { l } } { 2 \pi \varepsilon } \mathrm { l n } \frac { \sqrt { d ^ { 2 } \rho ^ { 2 } + a ^ { 4 } - 2 \rho d a ^ { 2 } \cos \phi } } { \sqrt { a ^ { 2 } \rho ^ { 2 } + a ^ { 2 } d ^ { 2 } - 2 \rho d a ^ { 2 } \cos \phi } }$ 

导体圆柱面上的感应电荷面密度为

$$
\rho_ {S} = - \varepsilon \frac {\partial \varphi}{\partial \rho} \bigg | _ {\rho = a} = - \frac {\rho_ {l} (d ^ {2} - a ^ {2})}{2 \pi a (a ^ {2} + d ^ {2} - 2 a d \cos \phi)}
$$

导体圆柱面上单位长度的感应电荷为

高数（第七版）上册381页（105式）

$$
\rho_ {i n} = \int_ {S} \rho_ {S} \mathrm {d} S = - \frac {\rho_ {l} (d ^ {2} - a ^ {2})}{2 \pi a} \int_ {0} ^ {2 \pi} \frac {a \mathrm {d} \phi}{a ^ {2} + d ^ {2} - 2 a d \cos \phi} = - \rho_ {l}
$$

导体圆柱面上单位长度的感应电荷与所设置的镜像电荷相等。

# 两平行圆柱导体的电轴

问题：如图1所示， 两平行导体圆柱的半径均为 $\pmb { a }$ ，两导体轴线间距为 $2 h$ ，单位长度分别带电荷 $\rho _ { l }$ 和 $- \rho _ { l }$ o

特点：由于两圆柱带电导体的电场互相影响，使导体表面的电荷分布不均匀，相对的一侧电荷密度大， 而相背的一侧电荷密度较小。

分析方法：将导体表面上的电荷用线密度分别为 $\pm \rho _ { l }$ 、 且相距为2b 的两根无限长带电细线来等效替代， 如图 2所示。

![image](images/559f40d1a648817ccb7af59651529ac7daa935909aacaf5984f1ada32ffaa2ed.jpg)



图1 两平行圆柱导体


![image](images/91b212bf7864c1f81b0c7f7259705b7b208a8dba00925ede97869a478363322d.jpg)



图2 两平行圆柱导体的电轴


# 利用线电荷与接地导体圆柱面的镜像确定

由 $d ^ { \prime } = \frac { a ^ { 2 } } { d } \Longrightarrow \ ( h - b ) ( h + b ) = a ^ { 2 }$ 

$$
\Longrightarrow b = \sqrt {h ^ {2} - a ^ {2}}
$$

![image](images/0669cc744ca5a9688193744220ea17abd3cbd56eb00e454a9212216750ff8fce.jpg)



图2 两平行圆柱导体的电轴


通常将带电细线的所在的位置称为圆柱导体的电轴，因而这种方法又称为电轴法。

思考：能否用电轴法求解半径不同的两平行圆柱导体问题？

![image](images/aa3d92136a8e07bda10a861305381951981ce12a365eea59cbda9147d705f4f8.jpg)


例3.5.3一根与地面平行架设的圆柱导体,半径为 $a$ ,悬挂高度为 $h$ ，如图3.5.16所示。（1）证明：单位长度上圆柱导线与地面间的电容为 $C _ { 0 } =$ ar(/a)；（2）若导线与地面间的电压为Un，证明：地面对单位长度导线的 $\frac { 2 \pi \varepsilon _ { 0 } } { \operatorname { a r c c o s h } ( h / a ) }$ $U _ { \mathfrak { d } }$ 

作用力 $F _ { 0 } = \frac { \pi \epsilon _ { 0 } U _ { 0 } ^ { 2 } } { [ \operatorname { a r c c o s h } ( h / a ) ] ^ { 2 } ( h ^ { 2 } - a ^ { 2 } ) ^ { 1 / 2 } } \circ$ 

![image](images/bb961d75f77abd9416e29e598b06d45b060d1d04d1197ea6d907c18e695608c6.jpg)



图3.5.16平行于地面的



圆柱导线


![image](images/dfdd67705dd06e8ffbd19ea40eb9d693f9adfeca1bae055a521e05fb653902fc.jpg)



图3.5.17平行于地面的圆


柱导线的镜像

$$
\begin{array}{l} \varphi_ {0} = \frac {q _ {l}}{2 \pi \varepsilon_ {0}} \ln \frac {1}{a - (h - b)} - \frac {q _ {l}}{2 \pi \varepsilon_ {0}} \ln \frac {1}{b + (h - a)} \\ = \frac {q _ {l}}{2 \pi \varepsilon_ {0}} \ln \frac {\sqrt {h ^ {2} - a ^ {2}} + (h - a)}{\sqrt {h ^ {2} - a ^ {2}} - (h - a)} \\ = \frac {q _ {l}}{2 \pi \varepsilon_ {0}} \ln \frac {\sqrt {h ^ {2} - a ^ {2}} + h}{a} = \frac {q _ {l}}{2 \pi \varepsilon_ {0}} \ln \left[ \sqrt {\left(\frac {h}{a}\right) ^ {2} - 1} + \frac {h}{a} \right] \\ \end{array}
$$

![image](images/9d0c17767a4f1637092f66da44b516d7c6968e8a3a883f42d8a931308d0e26a5.jpg)


因 $x > 1$ 时,有 $\ln ( { \sqrt { x ^ { 2 } - 1 } } + x ) = \operatorname { a r c c o s h } ( x )$ ,故上式可改写为

$$
\varphi_ {0} = \frac {q _ {l}}{2 \pi \varepsilon_ {0}} \operatorname {a r c c o s h} \left(\frac {h}{a}\right)
$$

$$
C _ {0} = \frac {q _ {l}}{\varphi_ {0}} = \frac {2 \pi \varepsilon_ {0}}{\operatorname {a r c c o s h} (h / a)}
$$

（2）导线单位长度上的电场能量为

$$
W _ {\mathrm {e}} = \frac {1}{2} C _ {0} U _ {0} ^ {2} = \frac {\pi \varepsilon_ {0} U _ {0} ^ {2}}{\operatorname {a r c c o s h} (h / a)}
$$

利用虚位移法，可得地面对导线单位长度的作用力为

$$
\begin{array}{l} F _ {0} = \left. \frac {\partial W _ {\mathrm {e}}}{\partial h} \right| _ {U _ {0} \text {不 变}} = \frac {\partial}{\partial h} \left[ \frac {\pi \varepsilon_ {0} U _ {0} ^ {2}}{\operatorname {a r c c o s h} (h / a)} \right] \\ = \frac {\pi \varepsilon_ {0} U _ {0} ^ {2}}{\left[ \operatorname {a r c c o s h} (h / a) \right] ^ {2} \left(h ^ {2} - a ^ {2}\right) ^ {1 / 2}} \\ \end{array}
$$

# 点电荷与无限大电介质平面的镜像

问题：如图 1 所示，介电常数分别为 $\varepsilon _ { 1 }$ 和 $\varepsilon _ { 2 }$ 的两种不同电介质的分界面是无限大平面，在电介质 1 中有一个点电荷q，距分界平面为h 。

特点：在点电荷的电场作用下，电介质产生极化，在介质分界面上形成极化电荷分布。此时，空间中任一点的电场由点电荷与极化电荷共同产生。

分析方法：计算电介质 1 中的电位时，用位于介质 2 中的镜像电荷来代替分界面上的极化电荷，并把整个空间看作充满介电常数为 $\mathcal { E } _ { 1 }$ 的均匀介质，如图2所示。

![image](images/3470c534a4ba95d2c9d38ea40bec3cc446daa5d9f86ed87f95dab4d0e7831494.jpg)



图1 点电荷与电介质分界平面


![image](images/e73489ae4ee8879d9cb6fd5cd27f57a0ed44481ba1e2f10ee6acc0381c4efd78.jpg)



图2 介质1的镜像电荷


$\frac { \partial } { \partial x } \frac { \partial } { \partial { \boldsymbol { \Sigma } } } : \nabla ^ { 2 } \varphi _ { 1 } = - \frac { \rho } { \varepsilon } \delta \big ( \boldsymbol { x } , \boldsymbol { y } , z - h \big ) , ( z \geq 0 )$ 

方程 $\nabla ^ { 2 } \varphi _ { 2 } = 0 , ( z \leq 0 )$ 

边界条件 lx²+y²+2²→ $\varphi { \frac { \scriptstyle } { 1 { \boldsymbol { x } } ^ { 2 } + y ^ { 2 } + z ^ { 2 } \to \infty } } = 0$ 

$$
\varphi_ {1} \big | _ {z = 0} = \varphi_ {2} \big | _ {z = 0}
$$

$$
\left. \varepsilon_ {1} \frac {\partial \varphi_ {1}}{\partial z} \right| _ {z = 0} = \left. \varepsilon_ {2} \frac {\partial \varphi_ {2}}{\partial z} \right| _ {z = 0}
$$

![image](images/e11edcc0973624d912953b5378c67586d27bc48b690daad826b36e3bfe5de595.jpg)



图1 点电荷与电介质分界平面


# 介质1中的电位为

$$
\varphi_ {1} (x, y, z) = \frac {1}{4 \pi \varepsilon_ {1}} \left[ \frac {q}{\sqrt {x ^ {2} + y ^ {2} + (z - h) ^ {2}}} + \frac {q ^ {\prime}}{\sqrt {x ^ {2} + y ^ {2} + (z + h) ^ {2}}} \right] \qquad (z \geq 0)
$$

计算电介质 2 中的电位时，用位于介质 1 中的镜像电荷来代替分界面上的极化电荷，并把整个空间看作充满介电常数为 $ { \varepsilon } _ { 2 }$ 的均匀介质，如图 3所示。介质2中的电位为

![image](images/9a5bf16ac925cdfd636827483dbc254260b588939bc13ea2f67a671a29571a78.jpg)



图3 介质2的镜像电荷


$$
\varphi_ {2} (x, y, z) = \frac {1}{4 \pi \varepsilon_ {2}} \frac {q + q ^ {\prime \prime}}{\sqrt {x ^ {2} + y ^ {2} + (z - h) ^ {2}}} \quad (z \leq 0)
$$

利用电位满足的边界条件

$$
\left. \varphi_ {1} \right| _ {z = 0} = \left. \varphi_ {2} \right| _ {z = 0} \qquad \left. \varepsilon_ {1} \frac {\partial \varphi_ {1}}{\partial z} \right| _ {z = 0} = \left. \varepsilon_ {2} \frac {\partial \varphi_ {2}}{\partial z} \right| _ {z = 0}
$$

${ \left\{ \begin{array} { l l } { { \cfrac { 1 } { \varepsilon _ { 1 } } } ( q + q ^ { \prime } ) = { \cfrac { 1 } { \varepsilon _ { 2 } } } ( q + q ^ { \prime \prime } ) } \\ { q - q ^ { \prime } = q + q ^ { \prime \prime } } \end{array} \right. } \Longrightarrow { \left\{ \begin{array} { l l l } { q ^ { \prime } = { \cfrac { \varepsilon _ { 1 } - \varepsilon _ { 2 } } { \varepsilon _ { 1 } + \varepsilon _ { 2 } } } q } \\ { q ^ { \prime \prime } = - { \cfrac { \varepsilon _ { 1 } - \varepsilon } { \varepsilon _ { 1 } + \varepsilon } } q } \end{array} \right. }$ a可得到 ε2

说明：对位于无限大平表面介质分界面附近、且平行于分界面的无限长线电荷（单位长度带），其镜像电荷为

$$
\rho_ {l} ^ {\prime} = \frac {\varepsilon_ {1} - \varepsilon_ {2}}{\varepsilon_ {1} + \varepsilon_ {2}} \rho_ {l}, \rho_ {l} ^ {\prime \prime} = - \frac {\varepsilon_ {1} - \varepsilon_ {2}}{\varepsilon_ {1} + \varepsilon_ {2}} \rho_ {l}
$$

# 线电流与无限大磁介质平面的镜像

问题：如图1所示，磁导率分别为 $\mu _ { 1 }$ 和 $\mu _ { 2 }$ 的两种均匀磁介质的分界面是无限大平面，在磁介质1中有一根无限长直线电流平行于分界平面，且与分界平面相距为h。

特点：在直线电流I 产生的磁场作用下，磁介质被磁化，在分界面上有磁化电流分布，空间中的磁场由线电流和磁化电流共同产生。

分析方法：在计算磁介质1中的磁场时，用置于介质2中的镜像线电流来代替分界面上的磁化电流，并把整个空间看作充满磁导率为 $\mu _ { 1 }$ 的均匀介质，如图2所示。

![image](images/ad874b2eb259d7e8064ef846f2f91d284e0f61628bbb2b322f7d380fd6d7ae3e.jpg)



图1 线电流与磁介质分界平面


![image](images/caa1a802df6305fefca64b881bc3f61d19256217798f1bb2a68875bf17959ad3.jpg)



图2 磁介质1的镜像线电流


在计算磁介质2中的磁场时， 用置于介质1中的镜像线电流来代替分界面上的磁化电流，并把整个空间看作充满磁导率为 $\mu _ { 2 }$ 的均匀介质，如图3所示。

因为电流沿y轴方向流动，所以矢量磁位只有y分量，则磁介质1和磁介质2中任一点的矢量磁位分别为

![image](images/97a2cba9e9685299dd90454326898fe0247fdd01d3a33a14a74a35128272131e.jpg)



图3 磁介质2的镜像线电流


$$
\begin{array}{l} A _ {1} = \frac {\mu_ {1} I}{2 \pi} \ln \frac {1}{\sqrt {x ^ {2} + (z - h) ^ {2}}} + \frac {\mu_ {1} I ^ {\prime}}{2 \pi} \ln \frac {1}{\sqrt {x ^ {2} + (z + h) ^ {2}}} (z \geq 0) \\ A _ {2} = \frac {\mu_ {2} (I + I ^ {\prime \prime})}{2 \pi} \ln \frac {1}{\sqrt {x ^ {2} + (z - h) ^ {2}}} \quad (z \leq 0) \\ \end{array}
$$

# 利用矢量磁位满足的边界条件

$$
\left. A _ {1} \right| _ {z = 0} = \left. A _ {2} \right| _ {z = 0}, \left. \frac {1}{\mu_ {1}} \frac {\partial A _ {1}}{\partial z} \right| _ {z = 0} = \left. \frac {1}{\mu_ {2}} \frac {\partial A _ {2}}{\partial z} \right| _ {z = 0}
$$

1 2( ) ( )I I I I + = +  $\left\{ { \begin{array} { l } { { \boldsymbol { I } } ^ { \prime } = { \frac { \mu _ { 2 } - \mu _ { 1 } } { \mu _ { 2 } + \mu _ { 1 } } } { \boldsymbol { I } } } \\ { { \boldsymbol { I } } ^ { \prime \prime } = - { \frac { \mu _ { 2 } - \mu _ { 1 } } { \mu _ { 2 } + \mu _ { 1 } } } { \boldsymbol { I } } } \end{array} } \right.$ 可得到I I I I − = + 

故 A $\mathsf { \Pi } _ { 1 } = \frac { \mu _ { 1 } I } { 2 \pi } \ln \frac { 1 } { \sqrt { x ^ { 2 } + \left( z - h \right) ^ { 2 } } } + \frac { \mu _ { 1 } ( \mu _ { 2 } - \mu _ { 1 } ) I } { 2 \pi ( \mu _ { 2 } + \mu _ { 1 } ) } \ln \frac { 1 } { \sqrt { x ^ { 2 } + \left( z + h \right) ^ { 2 } } }$ n (z≥0)

$$
A _ {2} = \frac {\mu_ {1} \mu_ {2} I}{\pi \left(\mu_ {2} + \mu_ {1}\right)} \ln \frac {1}{\sqrt {x ^ {2} + (z - h) ^ {2}}} \quad (z \leq 0)
$$

相应的磁场可由 $\overrightarrow { B } = \nabla \times \overrightarrow { A }$ 求得。

例3.5.4空气中有一根通有电流I的直导线平行于铁板平面,与铁表面距离为 $h$ ,如图3.5.24所示。求空气中任意一点的磁场。

![image](images/b91dc152aff58583629741248544a8490a63c726cb0f97798d3278766f6d0a57.jpg)



图3.5.24直线电流与铁板平面


![image](images/e2c09be5b89fecb7a062e43c221721092f42266ff4845b924f9d141b5daeb8c3.jpg)



3.5.25直线电流对无限大铁板平面的镜像


![image](images/44a7f0f7bd600836a0dbb12a37acebfe22610a051755dd359551e64a3bf2c420.jpg)


# 利用例3.3.2得出的一根无限长直线电流的矢量磁位计算公式

$$
\boldsymbol {A} = e _ {z} \frac {\mu_ {0} I}{2 \pi} \ln \left(\frac {\rho_ {0}}{\rho}\right)
$$

得到任意一点 $P ( x , y )$ 的矢量磁位为

$$
\boldsymbol {A} = e _ {z} \frac {\mu_ {0} I}{2 \pi} \ln \left(\frac {\rho_ {0}}{\rho_ {1}}\right) + e _ {z} \frac {\mu_ {0} I}{2 \pi} \ln \left(\frac {\rho_ {0}}{\rho_ {2}}\right) = e _ {z} \frac {\mu_ {0} I}{2 \pi} \ln \frac {\rho_ {0} ^ {2}}{\rho_ {1} \rho_ {2}}
$$

式中

$$
\rho_ {1} = \left[ x ^ {2} + (y - h) ^ {2} \right] ^ {1 / 2}, \quad \rho_ {2} = \left[ x ^ {2} + (y + h) ^ {2} \right] ^ {1 / 2}
$$

![image](images/340a1c12aeee58728e3629d13b8c02cedb891db88128f0cfaf28e79c80f158f0.jpg)


因此，点 $P ( x , y )$ 的磁感应强度为

$$
\begin{array}{l} \boldsymbol {B} = \boldsymbol {\nabla} \times \boldsymbol {A} = e _ {x} \frac {\partial A _ {z}}{\partial y} - e _ {y} \frac {\partial A _ {z}}{\partial x} \\ \mu_ {0} I \begin{array}{l} = - e _ {x} \frac {\mu I _ {0}}{2 \pi} \left[ \frac {y + h}{x ^ {2} + (y + h) ^ {2}} + \frac {y - h}{x ^ {2} + (y - h) ^ {2}} \right] + \\ e _ {y} \frac {\mu I _ {0}}{2 \pi} \left[ \frac {x}{x ^ {2} + (y + h) ^ {2}} + \frac {x}{x ^ {2} + (y - h) ^ {2}} \right] \end{array} \\ \end{array}
$$

+ 分离变量法是求解边值问题的一种经典方法

分离变量法解题的基本思路：

将偏微分方程中含有n个自变量的待求函数表示成n个各自只含一个变量的函数的乘积，把偏微分方程分解成n个常微分方程，求出各常微分方程的通解后，把它们线性叠加起来，得到级数形式解，并利用给定的边界条件确定待定常数。

中 分离变量法的理论依据是惟一性定理

