Full length article 

# Research on efficient braille recognition based on the pair-U-shaped micro-nano optical fiber fingerprint-like tactile sensors

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/877e29364e9caac5f505e8d466373f8580993933aeb9818b8526f05865bb6725.jpg)


Ling Huang<sup>a</sup>, Binbin Luo<sup>a, *</sup>, Xue Zou<sup>a,b, *</sup>, Decao Wu<sup>a</sup>, Fudan Chen<sup>a</sup>, Zhihai Liu<sup>a</sup>, Mingfu Zhao<sup>a</sup> 

a Chongqing Key Laboratory of Optical Fiber Sensor and Photoelectric Detection, Chongqing University of Technology, Chongqing 400054, China 

$^{b}$ School of Communications and Information Engineering, Chongqing University of Posts and Telecommunications, Chongqing 400065, China 

# ARTICLEINFO

Keywords: 

U-shaped micro-nano fiber 

Tactile sensor 

Fingerprint-like 

Braille recognition 

Long Short-Term Memory 

# ABSTRACT

Tactile sensors are essential for capturing touch information, yet existing sensors struggle to accurately mimic human pressure and motion perception. This study introduces a novel design resembling a fingerprint, featuring a pair-U-shaped flexible optical fiber tactile sensor, and assesses its efficacy in braille input interactions. Constructed from 3D-printed elastomeric resin, the sensor incorporates a bilayer structure that mirrors a fingerprint pattern, with interlocking microstructures and encapsulated pair-U-shaped micro-nano-optical fibers (MNF) within a polydimethylsiloxane (PDMS) layer. These design elements allow these two MNF sensing channels to achieve synchronization, enhancing durability and sensitivity $(66.08\% \mathrm{N}^{-1}$ and $65.59\% \mathrm{N}^{-1})$ , quickening response $(84.17 / 17.49~\mathrm{ms})$ and recovery time $(58.31 / 10.02~\mathrm{ms})$ for detecting braille surfaces. Utilizing the Long Short-Term Memory (LSTM) algorithm significantly boosts the accuracy of braille character recognition. Posttraining, the sensor achieved a $97.10\%$ recognition rate for 26 English letters under varying speeds and pressures. Moreover, the recognition rate for letters with similar features (B/K, F/M, G/X, H/U) improved to $98.58\%$ , underscoring the sensor's effectiveness in braille recognition. This innovative approach holds potential for applications in braille reading, surface sensing, and related areas. 

# 1. Introduction

In modern society, there is an increasing focus on enhancing information exchange for those who are visually impaired or blind [1]. According to the World Health Organization, there were approximately 43 million blind individuals globally in 2020, with over 17.3 million residing in China, as reported by the country's seventh census [2]. These individuals often struggle with reading and writing due to their reliance on touch for reading braille. However, learning braille is intricate, necessitating considerable training and specific reading tools [3]. Regrettably, limited societal awareness has slowed the progress of braille as a vital means of communication. Traditional braille recognition methods typically involve manually identifying braille feature points, which is laborious and complicates the accuracy of recognition results [4]. Consequently, developing an accurate and user-friendly haptic-centered braille recognition device is essential for the education of the blind. 

In this context, the application of haptic technology presents new 

opportunities for braille recognition. By integrating sophisticated tactile sensors and artificial intelligence, innovative and precise tactile braille recognition devices have been created. These devices offer smarter and more efficient solutions for the visually impaired to access and share information. For instance, Niu et al. [5] introduced a capacitive tactile sensor featuring an interlocking asymmetric nanocone structure, which effectively amplifies tactile stimuli. This enhancement was achieved using simple melt infiltration and commercial cone-shaped nanoporous anodic aluminum oxide technology, improving tactile feedback and the accuracy and efficiency of braille recognition. Gao et al. [6] explored a piezoresistive- piezoelectric dual-mode tactile sensor that merged the benefits of both types to improve overall tactile sensing performance. Integrating piezoelectric and resistive sensing mechanisms, this sensor provided higher sensitivity and resolution, meeting the demands of braille recognition more effectively. Cao et al. [7] developed a multilayered bionic structure using single-walled carbon nanotubes, polydimethylsiloxane (PDMS), polyethylene, and micropyramid arrays to recognize object surface textures, capable of detecting features as small 

全文

# 基于对U形微纳光纤指纹状触觉传感器的高效盲文识别研究

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/fe2f7e680a45af4679432610b8799063ea9d503444bf3f1ae7ca63ec767fb703.jpg)


黄凌 $^{a}$ , 罗彬彬 $^{a, *}$ , 邹雪 $^{a,b,*}$ , 吴德操 $^{a}$ , 陈福丹 $^{a}$ , 刘志海 $^{a}$ , 赵明福 $^{a}$ 

$^{a}$ Chongqing Key Laboratory of Optical Fiber Sensor and Photoelectric Detection, Chongqing University of Technology, Chongqing 400054, China $^{b}$ School of Communications and Information Engineering, Chongqing University of Posts and Telecommunications, Chongqing 400065, China 

# 文章信息

# Keywords:

U形微纳纤维触觉传感器类

指纹盲文识别长短期记忆

# 摘要

触觉传感器对于捕捉触摸信息至关重要，然而现有传感器难以准确模拟人类的压力与运动感知。本研究提出了一种仿指纹的新型设计，采用一对U形柔性光纤触觉传感器，并评估其在盲文输入交互中的效能。该传感器由3D打印的弹性树脂制成，采用仿指纹图案的双层结构，包含互锁微结构以及封装在聚二甲基硅氧烷（PDMS）层内的一对U形微纳光纤（MNF）。这些设计使两个MNF传感通道实现同步，提升了耐用性与灵敏度（ $66.08\% \, \mathrm{N}^{-1}$ 和 $65.59\% \, \mathrm{N}^{-1}$ ），并缩短了检测盲文表面的响应时间（84.17/17.49毫秒）与恢复时间（58.31/10.02毫秒）。利用长短期记忆（LSTM）算法显著提高了盲文字符识别的准确率。训练后，传感器在不同速度和压力下对26个英文字母的识别率达到 $97.10\%$ 。此外，对特征相似字母（B/K、F/M、G/X、H/U）的识别率提升至 $98.58\%$ ，突显了该传感器在盲文识别中的有效性。这一创新方法在盲文阅读、表面传感及相关领域具有应用潜力。

# 1. 引言

在现代社会，人们越来越关注如何增强视障或失明人士的信息交流能力[1]。根据世界卫生组织的数据，2020年全球约有4300万盲人，而中国第七次人口普查显示，其中超过1730万居住在中国[2]。由于依赖触摸阅读盲文，这些人士在读写方面常面临困难。然而，学习盲文过程复杂，需要大量训练和专门的阅读工具[3]。遗憾的是，社会认知的不足延缓了盲文作为重要交流手段的发展进程。传统的盲文识别方法通常涉及手动识别盲文特征点，这种方法既费力又影响识别结果的准确性[4]。因此，开发一种准确且用户友好的、以触觉为中心的盲文识别设备，对于盲人教育至关重要。

盲文识别的机遇。通过集成先进的触觉传感器和人工智能，创新且精确的触觉盲文识别设备得以问世。这些设备为视障人士获取和分享信息提供了更智能、更高效的解决方案。例如，Niu等人[5]介绍了一种具有互锁不对称纳米锥结构的电容式触觉传感器，能有效放大触觉刺激。这一增强效果通过简单的熔融渗透技术和商用锥形纳米多孔阳极氧化铝技术实现，从而提升了触觉反馈以及盲文识别的准确性和效率。Gao等人[6]探索了一种压阻-压电双模触觉传感器，融合了两类传感器的优势，以提升整体触觉传感性能。该传感器结合压电和电阻传感机制，提供了更高的灵敏度和分辨率，更有效地满足了盲文识别的需求。Cao等人[7]开发了一种多层仿生结构，采用单壁碳纳米管、聚二甲基硅氧烷（PDMS）、聚乙烯和微金字塔阵列来识别物体表面纹理，能够检测小至

在此背景下，触觉技术的应用带来了新的

E-mail addresses: luobinbin@cqut.edu.cn (B. Luo), zouxue@cqut.edu.cn (X. Zou). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/c0fd451c26971b8aebb56d6a2deb2bf439a2e2f4148220a158b5b052c5388847.jpg)



Fig. 1. Schematic diagram of a sensor that simulates the skin of a finger: (a) Structural and functional characteristics of a human fingertip; (b) the pair-U-shaped tactile sensing structure and braille recognition process.


as $15\mu \mathrm{m}\times 15\mu \mathrm{m}$ and standard braille characters. Their findings indicated that this multilayer structure greatly enhances surface texture recognition. Similarly, Tang et al. [8] designed a sensitive and cost-effective flexible piezoresistive sensor for braille recognition by combining controlled graphene nanowall (GNW) wrinkles with PDMS elastomers. Additionally, Zhu et al. [9] created a durable and flexible sliding haptic sensor for tactile detection of sub-millimeter and millimeter-scale patterns by contact with an object surface. Despite their impressive performance in braille recognition, these tactile sensors cannot extract one-to-one braille point feature signals with a single swipe. Furthermore, the mentioned braille recognition sensors, which are typically flexible electronic tactile sensors, including those based on piezoresistive [10], piezoelectric [11], piezocapacitive [12,13], and triboelectric [14,15] effects, face challenges such as parasitic effects, electronic channel crosstalk, and electromagnetic noise sensitivity. 

Fiber-optic flexible tactile sensors are known for their integrated sensing capabilities, ultra-thin and ultra-lightweight construction, high speed, high sensitivity, and resistance to electromagnetic interference. Among these, micro-nano optical fibers (MNF) are particularly notable due to their similarity in size to human nerve fibers, strong evanescent field properties, and mechanical flexibility. The photoconductive properties of MNF are crucial for detecting various parameters such as pressure, strain, bending, and vibration, making them highly responsive to external disturbances. Yao et al. [16] demonstrated e a single optical microfiber enabled tactile sensor that elucidates the pressure-sensing properties of MNF, providing important theoretical support for the construction of high sensitivity and fast response tactile sensors based on MNF. Zhang et al. [17] developed an opto-bionic skin by embedding MNF with a diameter of $0.8\mu \mathrm{m}$ into a thin layer of polydimethylsiloxane (PDMS), achieving ultra-high pressure sensitivity $(1870\mathrm{kPa}^{-1})$ , a very low detection limit $(7\mathrm{mPa})$ , and ultra-fast response time $(10~\mu \mathrm{s})$ significantly outperforming current flexible electronic skin technologies. Jiang et al. [18] used a resin/PDMS multilayer structure with fingerprint-like parallel ridged surfaces and varying stiffness to encapsulate MNF, mimicking the structural features of human finger skin. Tang et al. [19] created a tactile probe using a capillary tube and U-shaped MNF in PDMS, achieving high sensitivity in detecting object softness and hardness, with potential applications in telemedicine. Liu et al. [20] introduced a dual-channel MNF in a multilayer package to create integrated proximity and contact sensors capable of sensing humidity and tactile pressure, demonstrating their utility in human-machine interfaces. In recent years, MNF haptic sensors have used machine learning algorithms to assist in recognition, [21,22] which may provide more comprehensive technical support for applications such as healthcare, robotics, and human-machine interfaces. Wang et al. [23] designed an MNF-based gesture recognition wristband that accurately recognized gestures and interacted with a robotic hand, achieving a high recognition accuracy of $94\%$ across testers of different body types with the aid of a machine-learning algorithm. 

In this work, leveraging the unique advantages of MNF, we 

demonstrate a pair of flexible U-shaped MNF skin-like interlocking haptic sensors that enable intelligent braille sensing. To our knowledge, this is the first application of an MNF-based tactile sensor for braille recognition. The sensors' design includes a theoretical simulation to determine the optimal diameter of MNF at the critical dispersion turning point (DTP). A pair-U structure is then fabricated and embedded in two thin layers of PDMS film, with ring ridges bonded to the PDMS in an interlocking structure. This design mimics the interlocking structure of fingertip skin and fingerprints to enhance tactile stimulation. We introduce a long short-term memory (LSTM) neural network algorithm to enhance the recognition of braille feature signals. The effectiveness of this approach is assessed by simulating reading behavior. The sensing unit features a symmetrical dual-channel structure that provides excellent synchronization and responsiveness, capable of capturing corresponding braille feature signals and reproducing the braille with a single swipe. These developments contribute to advancing flexible tactile sensors and provide valuable insights into braille recognition and human-computer interaction. 

# 2. Principle and simulations

# 2.1. Sensor design

Skin is the most vital organ for tactile sensation and is one of our five primary senses [24]. Through our skin, we can discern the shape, hardness, texture, and roughness of objects. As illustrated in Fig. 1(a), the skin on human fingertips has a complex, multilayered structure comprising the epidermis, dermis, and subcutaneous tissue. The interlocking microstructure between the epidermis and dermis amplifies tactile stimuli and efficiently transmits them to the skin's mechanoreceptors. The outermost layer of the epidermis, which has a high modulus of elasticity, provides toughness. Additionally, fingerprint microstructures on its surface enhance friction and vibration, aiding in manipulation and texture perception [25]. As shown in Fig. 1(b), the sensor design, inspired by the unique biological microstructure of fingertip skin, consists of three primary components that replicate the skin layers of the fingertip. The upper and lower substrates serve as force-sensing layers, mimicking the circular ridge structure of the epidermis using 3D printing technology [26]. This microstructure is pivotal in boosting sensitivity and differentiating textures. The middle layer includes a double polydimethylsiloxane (PDMS) film that protects the pair-U-shaped MNF and enhances mechanical stimulation, thus increasing sensitivity and minimizing interference, attributable to the low Young's modulus, biocompatibility, and excellent optical properties of PDMS. The pair-U-shaped MNF receives force signals and converts them into dual-channel optical signals. It is positioned in a symmetrical structure to effectively recognize braille letters. This strong assembly results in a structure resembling fingertip skin, promoting robust adhesion between layers and enhancing overall structural stability. The different stiffness levels between the top elastic resin layer and the soft PDMS layer 


(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/512093b5633d0792171fc1913d697b69ab05557ac36bacb041214419f21c0812.jpg)



图1.模拟手指皮肤的传感器示意图：(a)人类指尖的结构与功能特征；(b)成对U形触觉传感结构及盲文识别过程。


作为15微米 $\times$ 15微米及标准盲文字符。他们的研究结果表明，这种多层结构极大地增强了表面纹理识别能力。同样，Tang等人[8]通过将可控石墨烯纳米壁（GNW）褶皱与PDMS弹性体结合，设计了一种用于盲文识别的灵敏且成本效益高的柔性压阻传感器。此外，Zhu等人[9]开发了一种耐用且灵活的滑动触觉传感器，用于通过与物体表面接触来检测亚毫米和毫米级图案的触觉。尽管这些触觉传感器在盲文识别方面表现出色，但它们无法通过单次滑动提取一对一的盲文点特征信号。此外，上述盲文识别传感器——通常是柔性电子触觉传感器，包括基于压阻[10]、压电[11]、压容[12,13]和摩擦电[14,15]效应的类型——面临着寄生效应、电子通道串扰和电磁噪声敏感性等挑战。

光纤柔性触觉传感器以其集成传感能力、超薄超轻结构、高速、高灵敏度和抗电磁干扰性而闻名。其中，微纳光纤（MNF）因其尺寸与人体神经纤维相似、强倏逝场特性和机械柔韧性而尤为突出。MNF的光导特性对于检测压力、应变、弯曲和振动等多种参数至关重要，使其对外部干扰高度敏感。Yao等人[16]展示了一种单根光学微纤维触觉传感器，阐明了MNF的压力传感特性，为构建基于MNF的高灵敏度快速响应触觉传感器提供了重要理论支持。Zhang等人[17]通过将直径为 $0.8\mu \mathrm{m}$ 的MNF嵌入薄层聚二甲基硅氧烷（PDMS）中，开发了一种光仿生皮肤，实现了超高压灵灵敏度（ $1870\mathrm{kPa}^{-1}$ ）、极低的检测限（ $7\mathrm{mPa}$ ）和超快响应时间（ $10~\mu \mathrm{s}$ ），显著优于当前的柔性电子皮肤技术。Jiang等人[18]采用具有指纹状平行脊表面和不同刚度的树脂/PDMS多层结构封装MNF，模拟了人体手指皮肤的结构特征。Tang等人[19]利用毛细管和U形MNF在PDMS中制作了触觉探针，实现了检测物体软硬度的高灵敏度，在远程医疗中具有潜在应用。Liu等人[20]引入多层封装中的双通道MNF，创建了能够感知湿度和触觉压力的集成接近与接触传感器，展示了其在人机界面中的实用性。近年来，MNF触觉传感器已借助机器学习算法辅助识别，[21,22]这可能为医疗保健、机器人和人机界面等应用提供更全面的技术支持。Wang等人[23]设计了一种基于MNF的手势识别腕带，能准确识别手势并与机械手交互，借助机器学习算法在不同体型的测试者中实现了 $94\%$ 的高识别准确率。

展示了一对灵活的U形微纳纤维（MNF）仿肤互锁触觉传感器，能够实现智能盲文感知。据我们所知，这是基于MNF的触觉传感器在盲文识别中的首次应用。该传感器的设计包括理论模拟，以确定在临界色散转折点（DTP）处MNF的最佳直径。随后制作了一对U形结构，并将其嵌入两层PDMS薄膜中，通过环形脊与PDMS以互锁结构结合。这一设计模仿了指尖皮肤和指纹的互锁结构，以增强触觉刺激。我们引入了长短期记忆（LSTM）神经网络算法来提升盲文特征信号的识别能力。通过模拟阅读行为评估了该方法的有效性。该传感单元采用对称双通道结构，具有出色的同步性和响应能力，能够捕获相应的盲文特征信号，并通过单次滑动重现盲文。这些进展有助于推动柔性触觉传感器的发展，并为盲文识别和人机交互提供了宝贵的见解。

# 2. 原理与仿真

# 2.1. Sensor design

皮肤是触觉感知最重要的器官，也是我们五种主要感官之一[24]。通过皮肤，我们能辨别物体的形状、硬度、纹理与粗糙度。如图1(a)所示，人类指尖皮肤具有复杂的多层结构，由表皮、真皮和皮下组织构成。表皮与真皮间的互锁微结构能放大触觉刺激，并将其高效传递至皮肤的机械感受器。表皮最外层具有高弹性模量，提供坚韧特性；其表面的指纹微结构则能增强摩擦与振动，辅助操作与纹理感知[25]。如图1(b)所示，受指尖皮肤独特生物微结构启发的传感器设计包含三个主要组件，分别复现指尖的皮肤层次：上下基板作为力感应层，通过3D打印技术模拟表皮的环形脊状结构[26]，这种微结构对提升灵敏度与纹理分辨能力至关重要；中间层采用双层聚二甲基硅氧烷（PDMS）薄膜，既保护U形配对微纳光纤（MNF），又通过PDMS的低杨氏模量、生物相容性及优异光学特性增强机械刺激响应，从而提高灵敏度并减少干扰。U形配对MNF负责接收力信号并将其转换为双通道光信号，其对称排布结构可有效识别盲文字符。这种紧密组装的类指尖皮肤结构能强化层间粘附力，提升整体稳定性。顶部弹性树脂层与柔软PDMS层间的刚度差异

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/c1efe2dd44037b4b7e01cb0d4f05aa610d6af920e8a39fc0063cb7f8c5f34ac5.jpg)



Fig. 2. Schematic diagram of the structure of dual-mode interference MNF.


enhance the sensor's tactile sensitivity to mechanical stimuli. All materials used in the sensor's fabrication are soft, making the multi-layered sensor highly flexible, easily bendable, and comfortably fitting around the finger. 

# 2.2. Principles and characteristics of MNF with U-shaped structure

Micro-nano fibers with an uninsulated drawn cone structure can be produced by fusing drawing cones from single-mode fibers. It has been demonstrated that when the diameter of the MNF is less than $12\mu \mathrm{m}$ , mode interference primarily occurs between the $\mathrm{HE}_{11}$ and $\mathrm{HE}_{12}$ modes [27]. Fig. 2 displays the structure of an MNF. The spectral intensity of the two-mode interference MNF shown in the figure can be expressed as [27]: 

$$
I = I _ {1 1} + I _ {1 2} + 2 \sqrt {I _ {1 1} I _ {1 2}} \cos \left(\frac {2 \pi}{\lambda} \Delta n _ {\text {e f f}} L + \Delta \varphi\right) \tag {1}
$$

where $I_{11}$ and $I_{12}$ are the light intensity of $\mathrm{HE}_{11}$ and $\mathrm{HE}_{12}$ modes, respectively, $\Delta n_{\text{eff}}$ is the difference in effective refractive index between modes, $\lambda$ is the wavelength, $L$ is the interference length, the phase difference variation $\Delta \varphi$ is expressed as [27]: 

$$
\Delta \varphi = \frac {2 \pi}{\lambda} \Delta n _ {\text {e f f}} L \left(\frac {\Delta L}{L} + \frac {\Delta (\Delta n _ {\text {e f f}})}{\Delta n _ {\text {e f f}}}\right) \tag {2}
$$

where $\Delta L$ is the change in the length of the MNF and $\Delta (\Delta n_{\mathrm{eff}})$ is the change in the difference in effective refractive index between modes. 

Based on the dispersion equation [28], we can calculate the effective refractive index (ERI) for the modes supported by MNF of various diameters. As depicted in Fig. 3(a), at a wavelength of $1550\mathrm{nm}$ , the ERI of the $\mathrm{HE}_{11}$ and $\mathrm{HE}_{12}$ modes shows a positive correlation with the diameter of the MNF. As demonstrated in Fig. 3(b), exploring the change in the 

interference peak's free spectral range (FSR) near $1550~\mathrm{nm}$ through simulations of MNF of different diameters reveals interesting correlations. As illustrated in Fig. 3(c), the FSR is positively correlated with diameters ranging from 3 to $10~{\mu\mathrm{m}}$ and negatively correlated with diameters between 2.2 and $2.5~{\mu\mathrm{m}}$ . This correlation informs the fabrication process of MNF, allowing us to estimate the MNF's diameter based on the FSR of its interference spectrum. Previous research has indicated that a dispersion turning point (DTP) microfiber with a diameter of approximately $2.2~{\mu\mathrm{m}}$ shows maximum pressure sensitivity at around $1590~\mathrm{nm}$ [29], and that when encapsulated in PDMS, the DTP drifts to around $1550~\mathrm{nm}$ . For temperature sensing, spectra in the long wavelength region show negligible variations [16]. Consequently, we selected MNFs with a diameter of approximately $2.2~{\mu\mathrm{m}}$ , coupled with light at $1550~\mathrm{nm}$ , to construct the sensing unit. 

In the context of fiber bending, changes in the waveguide's transmission direction are inevitable, potentially leading to bending loss or mode coupling. Experiments have demonstrated that fused-tapered MNF exhibit excellent homogeneity with minimal defects. These fibers can endure over $5\%$ tensile strain without fracturing, boasting an average tensile strength of up to 6 GPa—significantly surpassing the 3 GPa tensile strength of typical single-mode quartz fibers [30]. Notably, MNF maintains robust mechanical properties even when bent up to $180^{\circ}$ . Theoretical calculations indicate that for MNF with subwavelength diameters, bending losses are remarkably low at only $0.01~\mathrm{dB / mm}$ when the bending radius is within tens of microns [31]. This minimal loss ensures almost uninterrupted signal transmission in U-shaped MNF configurations. Additionally, a U-shaped structure not only extends the sensing range but also enhances resolution [19]. Thus, when fabricating U-shaped MNF, selecting the optimal bending radius based on the required dimensions can optimize its performance. 

# 2.3. Simulation and designation for the sensor structure

The finite element software COMSOL was utilized for parametric modeling and mechanical simulation of the haptic sensing unit. The simulations employed elastic resin as a hyperelastic material, characterized by two Mooney-Rivlin parameters, where $C_{10} = 3.7^* 10^5$ Pa, $C_{01} = 1.1^* 10^5$ Pa, bulk modulus $K = 1^* 10^7$ Pa, density $\rho = 1.1^* 10^4$ kg/m³, $C_{10}$ and $C_{01}$ are PDMS material parameters, respectively, representing the elastic modulus of stress and strain in the principal direction. We previously analyzed the impact of the thickness of the encapsulation material on stress distribution within the MNF plane [32]. Our results indicated that a thinner upper PDMS layer results in greater stress on the MNF plane. Additionally, a thinner upper annular ridge also leads to increased stress; however, the thickness of the lower PDMS and ring ridge has minimal impact on the stress experienced by the MNF plane. Consequently, various combinations of feature sizes within the package structure can be tailored to suit different tactile force scenarios. The interlocking structure enhances the strain-bending capability of the MNF, and the upper ring ridge augments the detection of vibration and 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/2e3cd787af156bc7d1663964d73d309ac6a9754985edd0eb5749794155165aff.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/5a973452e95cbb048ec15e55a1610121027047f5e81fc4be5505815190864a75.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/cde1a80ec2f34d7317d96eab9ab90688078406eb4fb0cd9d3a278c7795e2e963.jpg)



Fig. 3. (a) Change of effective refractive index versus MNF diameter for $\mathrm{HE}_{11}$ and $\mathrm{HE}_{12}$ modes at wavelength $1550\mathrm{nm}$ ; (b) Analog spectra of MNF with diameters of $10\mu \mathrm{m}$ , $5\mu \mathrm{m}$ and $2.2\mu \mathrm{m}$ ; (c) changes in FSR around $1550\mathrm{nm}$ for different diameters of MNF.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/4285f9e0b2d8f864a4c48d1f02d29c8e42ea8798eb9de623375350f5588e0f98.jpg)



图2.双模干涉MNF结构示意图


增强传感器对机械刺激的触觉灵敏度。传感器制造中使用的所有材料均为软质材料，使得多层传感器具有高度柔韧性、易于弯曲，并能舒适地贴合手指。

# 2.2. Principles and characteristics of MNF with U-shaped structure

采用单模光纤熔融拉锥可制备出无绝缘拉锥锥形结构的微纳光纤。研究表明，当MNF直径小于 $12\mu \mathrm{m}$ 时，模式干涉主要发生在 $\mathrm{HE}_{11}$ 和 $\mathrm{HE}_{12}$ 模式之间[27]。图2展示了MNF的结构。图中所示双模干涉MNF的光谱强度可表示为[27]:

$$
I = I _ {1 1} + I _ {1 2} + 2 \sqrt {I _ {1 1} I _ {1 2}} \cos \left(\frac {2 \pi}{\lambda} \Delta n _ {\text {e f f}} L + \Delta \varphi\right) \tag {1}
$$

其中 $I_{11}$ 和 $I_{12}$ 分别为 $\mathrm{HE}_{11}$ 和 $\mathrm{HE}_{12}$ 模式的光强， $\Delta n_{eff}$ 是模式间的有效折射率差， $\lambda$ 是波长， $L$ 是干涉长度，相位差变化 $\Delta \varphi$ 表示为 [27]：

$$
\Delta \varphi = \frac {2 \pi}{\lambda} \Delta n _ {\text {e f f}} L \left(\frac {\Delta L}{L} + \frac {\Delta (\Delta n _ {\text {e f f}})}{\Delta n _ {\text {e f f}}}\right) \tag {2}
$$

其中 $\Delta L$ 是MNF长度的变化， $\Delta (\Delta n_{\mathrm{eff}}$ 是模式间有效折射率差的变化。

根据色散方程[28]，我们可以计算出不同直径微纳光纤所支持模式的有效折射率（ERI）。如图3(a)所示，在 $1550\mathrm{nm}$ 波长下， $\mathrm{HE}_{11}$ 和 $\mathrm{HE}_{12}$ 模式的有效折射率与微纳光纤直径呈正相关。如图3(b)所示，通过探究

通过模拟不同直径微纳光纤在 $1550 \mathrm{~nm}$ 附近的干涉峰自由光谱范围（FSR），发现了有趣的相关性。如图3(c)所示，FSR与直径在3至 $10 \mu \mathrm{m}$ 范围内呈正相关，而在2.2至 $2.5 \mu \mathrm{m}$ 范围内呈负相关。这种相关性为微纳光纤的制备工艺提供了指导，使我们能够基于其干涉光谱的FSR估算光纤直径。先前研究表明，直径约 $2.2 \mu \mathrm{m}$ 的色散转折点（DTP）微纳光纤在约 $1590 \mathrm{~nm}$ 处具有最大压力灵敏度[29]，且当封装在PDMS中时，DTP会漂移至155 $0 \mathrm{~nm}$ 附近。对于温度传感，长波长区域的光谱变化可忽略不计[16]。因此，我们选择直径约 $2.2 \mu \mathrm{m}$ 的微纳光纤，结合 $1550 \mathrm{~nm}$ 波长的光，构建了传感单元。

在光纤弯曲的背景下，波导传输方向的改变不可避免，可能导致弯曲损耗或模式耦合。实验表明，熔融拉锥微纳光纤表现出优异的均匀性，缺陷极少。这些光纤可承受超过 $5\%$ 的拉伸应变而不断裂，平均拉伸强度高达6GPa——显著超过普通单模石英光纤3GPa的拉伸强度[30]。值得注意的是，即使弯曲角度达到 $180^{\circ}$ ，微纳光纤仍能保持强健的机械性能。理论计算表明，对于亚波长直径的微纳光纤，当弯曲半径在数十微米范围内时，弯曲损耗极低，仅为 $0.01\mathrm{dB / mm}[31]$ 。这种微小的损耗确保了U形微纳光纤结构中信号传输几乎不受干扰。此外，U形结构不仅能扩展传感范围，还能提高分辨率[19]。因此，在制备U形微纳光纤时，根据所需尺寸选择最佳弯曲半径可优化其性能。

# 2.3. Simulation and designation for the sensor structure

采用有限元软件COMSOL对触觉传感单元进行参数化建模与力学仿真。仿真中将弹性树脂视为超弹性材料，采用两个Mooney-Rivlin参数表征，其中 $C_{10} =$ 为 $3.7*10^{5}\mathrm{Pa}$ ， $C_{01} =$ 为 $1.1*10^{5}\mathrm{Pa}$ ，体积模量K=为 $1*10^{7}\mathrm{Pa}$ ，密度 $\rho =$ 为 $1.1*10^{4}\mathrm{kg/m^{3}}$ 。 $\mathrm{C_{10}}$ 和 $\mathrm{C_{01}}$ 分别为PDMS材料参数，代表主方向应力与应变的弹性模量。我们先前分析了封装材料厚度对MNF平面内应力分布的影响[32]。结果表明：上层PDMS越薄，MNF平面承受的应力越大；同时，上层环形凸缘越薄也会导致应力增加；而下层PDMS及环形凸缘厚度对MNF平面应力的影响甚微。因此，可通过调整封装结构中不同特征尺寸的组合来适配各类触压力场景。互锁结构增强了MNF的应变弯曲能力，而上层环形凸缘则提升了振动与

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/da9888222cdbd69f5851e7b0a0cf45140a299ab8b306d69f3a8ac602f80c8d89.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/e9733cbdc025f3fccefe52c3ac2cd4c47cb296429f13733e0cde3244c81c2281.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/f0b4a4a1c855fd74952448f315f6a1d880ac09eefd1e2e3ad3032a0191f59aaf.jpg)



图3.(a)在 $1550\mathrm{nm}$ 波长下， $\mathrm{HE}_{11}$ 和 $\mathrm{HE}_{12}$ 模式的有效折射率随MNF直径的变化；(b)直径为 $10~{\mu\mathrm{m}}$ 、 $5\mu \mathrm{m}$ 和 $2.2\mu \mathrm{m}$ 的MNF模拟光谱；(c)不同直径MNF在 $1550\mathrm{nm}$ 附近自由光谱范围(FSR)的变化。



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/e8791370c0828ccf8d306ea8377d649358c1c7a068ee4e53575be3549a3077a1.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/4dc02faf84d284561c1d4b3d03117543feb6752da42a0bf2dfcf8967313ca109.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/0c2411f202b472d07b753e7155aba47206e0617368bd7011659a745ad64c4fa8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/f2cc9b206bf61a4915e81ccd18c83ad82b253e1d775a999e73a39fc94ccad6da.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/9e83b3c7eb6d218096d1391340a71086e062d0a268bf41bf2af332d3ddb7c048.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/2023198e1e1249249953c0901a85eed3f827e8e6284ba2fc74c6cdfb85ffcdee.jpg)



Fig. 4. (a) Z-axis deformation under $1 - 10\mathrm{N}$ normal force; (b) Stress diagram under normal force; (c) Stress diagram under friction.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/4ebf8a9631d6339632a4aa05333e84489431a985150b3ff69ffcf568ec3580d1.jpg)



Fig. 5. Response of the sensor unit under finger press and sliding.



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/f0b4a856c0bd67135ad166c6833cc3c7a6e935385d48437ff04c021a9082399f.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/8c2ac466bd125e46c49b15cc1ba1ccb127c27275063c4195900546277dac0663.jpg)



Fig. 6. Mode field distribution in the MNF with a diameter of $2.2\mu \mathrm{m}$ (a) unbent; (b) bent with a radius of $2.2\mathrm{mm}$ .


tactile information by the MNF. After a comprehensive evaluation, we opted for a structure with an upper PDMS film thickness of $50~{\mu\mathrm{m}}$ and a lower PDMS film thickness of $100~{\mu\mathrm{m}}$ , with an upper ring ridge of 0.2 mm and a lower ring ridge of $0.4~\mathrm{mm}$ . 

The deformation of the sensing unit under a normal force of $1\mathrm{N}$ is simulated, as illustrated in Fig. 4(a). The layer containing the MNF exhibits a subtle multiscale bending pattern, indicating that the interlocked structure can induce significant micro-bending. The degree of bending progressively increases as the normal force is applied, resulting in an escalation in MNF bending. Furthermore, in a simulation applying both a $1\mathrm{N}$ normal force and a $0.5\mathrm{N}$ tangential force, the maximum stress occurs below the circumferential ridge under applied pressure $(\mathrm{F_z} = 1$ N). Conversely, when friction is introduced $(\mathrm{F_z} = 1\mathrm{N},\mathrm{F_x} = 0.5\mathrm{N})$ , the maximum stress shifts from the circumferential ridge area, and its magnitude increases. These simulation results demonstrate that the change in stress distribution significantly alters the sensing unit's response in both scenarios. In a preliminary experiment, an adult continuously scanned and pressed the sensor surface with their index finger. As shown in Fig. 5, the output waveform's intensity change is subtle when the finger presses but becomes markedly more pronounced during scanning, producing a burst of pulses. This suggests that the annular ridge on the top layer enhances friction during sliding movements, improving slip detection performance, similar to how human fingerprint ridges detect vibrational tactile information. 

To prevent signal crosstalk, given the braille bump spacing of 2-2.8 mm, and based on prior analysis and research, we selected a MNF with a diameter of approximately $2.2\mu \mathrm{m}$ and a bending radius of about $2.2\mathrm{mm}$ for the pair-U-shaped MNF sensor. Simulation results were obtained using COMSOL finite element software, as illustrated in Fig. 6, showing that the MNF remains unbent and light continues to propagate along the fiber core. It is observed that when the refractive indices of the PDMS and the fiber core are 1.40 and 1.4628, respectively, the evanescent field energy proportion is $26.14\%$ . This indicates that the PDMS layer retains the evanescent field energy of the fundamental mode more effectively than the air cladding, which retains only $2.69\%$ . This results in a higher transmission of light field energy in the form of evanescent waves close to the MNF surface. When the MNF bends, the mode field distribution shifts from core center symmetry to outer contour asymmetry, transforming the fundamental mode into a radiation mode. This transformation results in an increase in the leakage of light field energy, with the energy proportion rising to $82.29\%$ . This significant increase makes the sensor more sensitive to detecting micro-bending situations. 

# 2.4. Sensor fabrication

A flame-melting taper method was employed to create non-adiabatic mutation cones using an SM28 optical fiber. This fiber was placed on a vacuum adsorption stage with a pre-stretch speed of $120\mu \mathrm{m / s}$ and a pre-stretch distance of $12,000~{\mu\mathrm{m}}$ Tension was applied to stretch the fiber, reducing its diameter to the desired size. During the fiber-pulling 


(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/4547485f52bdc276d460b6b4925719e0b0c288169b155811256b75eb11b9be97.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/68e41ab346d63e9d84cec320d96479802aad4b13281bc6b7d3009b3887bebfb6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/9b5f6e6a261b98cbf1264b35cf0f18ad98eb42da91534b278d3b33108f19eb36.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/01754f7c68e1bfbd7151096189320791d40460d4ffd4d4d90f945f646e207d50.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/8c480e69525fa70abc333042ec235549c7a60eab5330e54f845ab37ccff9b1fd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/498fcec5046acfbd4bec10ca766d3febcf3de64162ae9cbe56ba3b8c6d2024d1.jpg)



图4.(a)1-10N法向力下的Z轴变形；(b)法向力下的应力分布图；(c)摩擦力下的应力分布图。


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/81853b7bb3999db8cf018ab0dab089737f40d2cdffe92cacb37b424a84b129ee.jpg)



图5.传感器单元在手指按压和滑动下的响应



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/f2902b3ddf6acf9e77c16a6dd7cce7000acac4c491282f4bf0f2c8d8ab22bdf4.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/5dc046f00b91dfd30551de7c7ef3ca38e0b4faf4f509fd49724cafb9d99968e7.jpg)



图6.直径为 $2.2\mu \mathrm{m}$ 的MNF中的模场分布：(a)未弯曲；(b)以 $2.2\mathrm{mm}$ 半径弯曲。


通过MNF获取触觉信息。经过全面评估，我们选择了上层PDMS薄膜厚度为 $50 \mu \mathrm{m}$ 、下层PDMS薄膜厚度为 $100 \mu \mathrm{m}$ 的结构，其中上层环形凸起为 $0.2 \mathrm{~mm}$ ，下层环形凸起为 $0.4 \mathrm{~mm}$ 。

在1N法向力作用下传感单元的变形情况如图4(a)所示进行模拟。含有微纳纤维的层呈现出微妙的多尺度弯曲形态，表明互锁结构能引发显著的微观弯曲。随着法向力的施加，弯曲程度逐步增强，导致微纳纤维弯曲加剧。此外，在同时施加1N法向力与0.5N切向力的模拟中，最大应力出现在受压圆周脊下方区域（ $\mathrm{F_z} = 1\mathrm{N}$ ）。而当引入摩擦力时（ $\mathrm{F_z} = 1\mathrm{N}$ ， $\mathrm{F_x} = 0.5\mathrm{N}$ ），最大应力从圆周脊区域转移，且应力幅值增大。这些模拟结果证明，应力分布的变化会显著改变两种场景下传感单元的响应特性。在初步实验中，成人受试者持续用食指按压并扫描传感器表面。如图5所示，手指按压时输出波形强度变化微弱，但在扫描过程中强度变化显著加剧，产生脉冲簇现象。这表明顶层环形脊能在滑动运动中增强摩擦，提升滑移检测性能，其原理类似于人类指纹脊对振动触觉信息的感知机制。

为防止信号串扰，考虑到盲文凸点间距为2-2.8毫米，并基于先前的分析与研究，我们为U形对偶MNF传感器选择了直径约2.2微米、弯曲半径约2.2毫米的MNF。通过COMSOL有限元软件进行仿真，结果如图6所示，表明MNF未弯曲时光仍沿纤芯传播。当PDMS与纤芯的折射率分别为1.40和1.4628时，可观察到倏逝场能量占比为 $26.14\%$ 。这说明PDMS层比仅保留 $2.69\%$ 能量的空气包层能更有效地保留基模的倏逝场能量，从而使更多光场能量以倏逝波形式在MNF表面附近传输。当MNF弯曲时，模场分布从纤芯中心对称转变为外轮廓不对称，基模转化为辐射模。这一转变导致光场能量泄漏增加，能量占比升至 $82.29\%$ 。该显著提升使传感器对微弯状态的检测更为敏感。

# 2.4. Sensor fabrication

采用火焰熔融拉锥法，利用SM28光纤制备非绝热突变锥。将光纤置于真空吸附平台上，预拉伸速度为 $120\mu \mathrm{m / s}$ ，预拉伸距离为 $12,000~\mu \mathrm{m}$ 。通过施加张力拉伸光纤，使其直径减小至目标尺寸。在拉锥过程中

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/c102c25b9ea6b5e93efb0344a4b161c51d782fa835ffd466b7ceacd54c9fc6f9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/40a781c14d29c2b23316cfd73c868f079c4103a1f2fb4edbe102c3f45a3dc64d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/e63fff621f13211166e365629c7fc8ae4acf180cbc0adb922ce5051e44bcd6e9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/53117b9e674c0b553ab03f84380873c8528bb17e77d80170ff0118803038a730.jpg)



Fig. 7. Sensor micrographs of (a) and (b) MNF with a diameter of $\sim 2.2\mu \mathrm{m}$ ; (c) pair-U-shaped micro-nano-fiber micrographs; (d) transmission spectra before and after encapsulation.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/e7428c1e1c9a9d5380ae731d84246b6d801de650d0fe3960774d09f57e2ab9d0.jpg)



Fig. 8. Sensing unit fabrication process of the pair-U-shaped MNF tactile sensing area.


process, a broadband light source with a wavelength range of $1500 - 1600\mathrm{nm}$ was introduced into the fiber. Spectrometers were utilized for spectral analysis, and the diameter of the fiber was estimated based on the FSR of the interference spectrum. Microscope images of the two MNFs and the pair-U-shaped MNF sensor are shown in Fig. 7(a-c), demonstrating that two MNFs with diameters of approximately $2.2\mu \mathrm{m}$ , a bending diameter of about $2.2\mathrm{mm}$ , a girdle taper length of roughly $2,500~{\mu\mathrm{m}}$ , and a spacing of $2\mathrm{mm}$ were successfully fabricated. The changes in transmission spectra before and after the encapsulation of the two MNFs are depicted in Fig. 7(d). It is observed that the high refractive index (1.40) of PDMS alters the waveguide mode structure, causing the two-mode interference phenomenon to disappear, resulting in an almost flat periodic spectrum for the encapsulated MNF. 

According to the designed parameters of the sensor structure, the integration process for the haptic sensor is outlined in Fig. 8. The pair-U-shaped MNFs were sandwiched between two PDMS films with thicknesses of $50\mu \mathrm{m}$ and $100\mu \mathrm{m}$ , respectively, and then cured at $50^{\circ}\mathrm{C}$ for $1\mathrm{h}$ to eliminate bubbles. Subsequently, the upper and lower ring ridges were fabricated using elastic resin, mimicking the microscopic structure of fingertip skin using 3D printing technology. The fingerprint-like top ring ridge, with a total diameter of $12\mathrm{mm}$ , ridge thickness of $0.2\mathrm{mm}$ , ridge width of $0.5\mathrm{mm}$ , and ridge spacing of $0.5\mathrm{mm}$ , closely approximates the adult fingerprint ridge line (spacing: $0.4 - 0.5\mathrm{mm}$ ; thickness: $0.2\mathrm{mm}$ ). The elastic resin layer was then securely bonded to the soft PDMS layer using room-temperature vulcanizing (RTV) adhesive, ensuring robust adhesion between the layers and enhancing the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/725e7a158e265880b7b0270081760b1bef912032ea825e42413b2dd8fb24a91e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/53fdafd285ce3505061b78eace37845d8f0ddfd6d9412c8cc2f5a194425f3312.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/64ec171af1e8f8c13172e70f8f6b89ec272b52455d93e4efda31d30123c21732.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/44702fec4d7aa18136fbec42a9847faa7f3fc6327c60a428645520e1db8c6302.jpg)



图7.传感器显微图：(a)和(b)直径为 $\sim 2.2\mu \mathrm{m}$ 的微纳光纤；(c)U形对微纳光纤显微图；(d)封装前后的透射光谱。


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/ef2035c8c2791de53dce624a04238ecba5573f2998346774b53fafc8b7ee6597.jpg)



图8.成对U形微纳光纤触觉传感区域的传感单元制备流程


过程中，将波长范围为 $1500 - 1600\mathrm{nm}$ 的宽带光源引入光纤。利用光谱仪进行光谱分析，并根据干涉谱的自由光谱范围（FSR）估算光纤直径。图7(a-c)展示了两根微纳光纤（MNF）以及成对U形MNF传感器的显微镜图像，表明成功制备了两根直径约 $2.2\mu \mathrm{m}$ 、弯曲直径约 $2.2\mathrm{mm}$ 、锥腰长度约 $2500~{\mu\mathrm{m}}$ 、间距为 $2\mathrm{mm}$ 的MNF。图7(d)描绘了两根MNF封装前后透射光谱的变化。可以观察到，PDMS的高折射率（1.40）改变了波导模式结构，导致双模干涉现象消失，从而使封装后的MNF呈现出近乎平坦的周期性光谱。

根据传感器结构的设计参数，触觉传感器的集成过程如图8所示。将一对U形微纳光纤夹在厚度分别为50微米和100微米的PDMS薄膜之间，随后在 $50\{\mathrm{v}^{*}\}$ C下固化1小时以消除气泡。接着，利用弹性树脂通过3D打印技术仿照指尖皮肤的微观结构，制作了上下环形脊。指纹状顶部环形脊的总直径为12毫米，脊厚度为0.2毫米，脊宽度为0.5毫米，脊间距为0.5毫米，高度接近成人指纹脊线（间距：0.4-0.5毫米；厚度：0.2毫米）。随后使用室温硫化胶将弹性树脂层牢固粘合到软质PDMS层上，确保层间牢固粘附并增强

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/33685e59ed701a3e98a1533102a18311d28f0addc101ea0cec9c40c3649fdb42.jpg)



Fig. 9. Diagram of the experimental system for mechanical property testing.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/16795499d2dac8d7082af043c654463f9ef7c09239cb6a40758a36cf69a110f1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/6674c185b2904b26f490a30447362d6910fc1b2ff5df02ccd4cd38db0cc551d4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/0f731ed853c78eb53b1a393bc52f8b4b81c6a7e5389caa0a85710345efd557c3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/5781e8c64a3951509adb66b95f1f9d7eec1a0ca483c984b8145fec14d7b94bee.jpg)



Fig. 10. Comparison and calibration of mechanical properties for MNF1 and MNF2 (a) spectral response for pressure of MNF1; (b) spectral response for pressure of MNF2; (c) sensitivities; (d) reproducibility.


mechanical stability of the sensor. This packaging design aims to maintain high sensitivity while providing necessary mechanical protection and environmental isolation, enabling it to function reliably in dynamic and complex application scenarios. 

# 3. Experimental results and discussion

# 3.1. Mechanical performances of the sensor

As depicted in Fig. 9, light from a broadband light source (ASE, 

CONOUER) is directed to the sensing unit via a coupler. Both static and dynamic pressures are applied using a precision dynamometer (MPT, Mark-10 ESM303). The modulated light intensity from the mechanical signal is then converted by a photodetector (PD, CONOUER, $200\mathrm{kHz}$ ) and relayed to an oscilloscope for real-time monitoring. 

Fig. 10(a) and (b) display the spectral response of MNF1 and MNF2 to varying pressure levels (0–1 N increment: 0.05 N; 1–10 N increment: 1 N) within the wavelength range of 1500–1600 nm, respectively. It is observed that the intensity of the transmission spectrum decreases with increasing pressure due to the enhanced micro-bending of the MNF. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/e9e5476cc9a56291842c1b3541fb186a0402ea01e1f1d09f952d49ff0e2061a5.jpg)



图9.机械性能测试实验系统示意图


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/fc156a9c9486c42f29dde2356efa07aa90d02893212cbfa8ee301d4566c4a6d1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/9bf1ebd9419385bca85db5e194f0af011cdb423c461f39baac020b85fe3bfd45.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/45a8d2f1a4364b87e81259166fb0ecb23e3d69371c40ff568552781b0f87715f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/c9d1f6632ba3d7163d1b9ff81e9f5b91e174119795273f086f22965358c85b85.jpg)



图10.MNF1与MNF2机械性能的对比与校准(a)MNF1对压力的光谱响应；(b)MNF2对压力的光谱响应；(c)灵敏度；(d)重复性。


传感器的机械稳定性。这种封装设计旨在保持高灵敏度的同时，提供必要的机械保护和环境隔离，使其能够在动态复杂的应用场景中可靠运行。

# 3. 实验结果与讨论

# 3.1. Mechanical performances of the sensor

如图9所示，来自宽带光源（ASE）的光，

CONOuer) 通过耦合器导向传感单元。静态和动态压力均使用精密测力计（MPT, Mark-10 ESM303）施加。随后，由机械信号调制的光强度通过光电探测器（PD, CONOuer, $200\mathrm{kHz}$ ）转换，并传输至示波器进行实时监测。

图10(a)和(b)分别展示了MNF1和MNF2在 $1500 - 1600\mathrm{nm}$ 波长范围内对不同压力水平（0-1N增量： $0.05\mathrm{N}$ ；1-10N增量：1N）的光谱响应。可以观察到，由于MNF微弯效应的增强，透射光谱的强度随压力增加而降低。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/759cc875ad0aa1368a3d2972fe985faac6ce62b48365a30361aa0c768427c77a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/32782645be590b716fb56705b4f8ae0905861f9f37c073d5b5fbf340d4730180.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/6eb5a43fcb8408fd6123d020581126f4ae9f0ace5aa3c4ca1f37e30671ba58e0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/5d4781615270c6e31daa0a320561a0ef28549cf67cb5b8a65f74a4a3312d7312.jpg)



Fig. 11. Comparison and calibration of mechanical properties for MNF1 and MNF2, (a) response/recovery time; (b) incremental pressure response curves; (c) repeatability tests.


Fig. 10(c) illustrates that at the wavelength of $1550\mathrm{nm}$ , the change in relative strength (the initial output under no pressure) corresponds to the applied normal force. The pressure sensitivity of MNF1 in the range of $0 - 1\mathrm{N}$ was $66.08\% \mathrm{N}^{-1}$ , and for MNF2, it was $65.59\% \mathrm{N}^{-1}$ . In the range of $2 - 10\mathrm{N}$ , the sensitivity for MNF1 dropped to $3.4\% \mathrm{N}^{-1}$ and for MNF2 to $2.87\% \mathrm{N}^{-1}$ , showing a high degree of consistency between the two sensing channels. The observed difference in sensitivity across different pressure ranges can be attributed to the sensor's saturation under larger force applications, which results in diminished sensitivity. Fig. 10(d) shows the pressure response curves of two duplicated sensing units, demonstrating a high correlation coefficient close to that of MNF1 and significant curve overlap. 

These results have affirmed the reliability and reproducibility of the sensors throughout their fabrication. To evaluate the response time and repeatability of the MNF sensor, a normal force gauge was utilized, applying a force of $1\mathrm{N}$ to the sensor surface. As depicted in Fig. 11(a), 

the sensor demonstrated an excellent transient response, with loading and unloading response times of 84.17 ms and 58.37 ms, respectively, and recovery times of 10.02 ms and 17.49 ms, respectively. Additionally, the recovery time was primarily influenced by the viscosity of the elastic resin material, a typical issue for flexible sensors. Nevertheless, the sensor proved capable of meeting the requirements for real-time detection of physical stimuli. 

When subjected to progressively increasing pressure levels, the transmitted light intensity decreased gradually, exhibiting stable and consistent fluctuations, as illustrated in Fig. 11(b). Even after 700 loading and unloading cycles, the output signals of the sensor remained stable, showing no notable performance degradation, as seen in Fig. 11 (c). This durability and consistency are due to the robust encapsulation of the MNF within the PDMS and the strong adhesion within the multilayer sensor structure. The sensor maintains a uniform pressure response with minimal fluctuations in baseline intensity, facilitating the 


Table 1 Comparison of MNF sensors in different shapes and packages.


<table><tr><td>Shape</td><td>Package Material</td><td>Micro structure</td><td>Force Election range</td><td>Sensitivity</td><td>Diameter</td><td>Response/Recovery Time</td></tr><tr><td>Straight[17]</td><td>PDMS</td><td>None</td><td>0–10 kPa</td><td>1870 kPa-1</td><td>0.8 μm</td><td>10 μs</td></tr><tr><td>Straight[20]</td><td>PDMS + CV</td><td>None</td><td>0–110 kPa</td><td>6.5 % kPa-1</td><td>1.3 μm 2 μm</td><td>110 ms/3s</td></tr><tr><td>U-shape[19]</td><td>PDMS + Capillary</td><td>None</td><td>0–20 N</td><td>0.0108 %/N</td><td>2.7 μm</td><td>&lt;1ms</td></tr><tr><td>U-shape[18]</td><td>PDMS + Resins</td><td>Parallel ring</td><td>0–20 N</td><td>5.4 %/N</td><td>1.2 μm</td><td>-</td></tr><tr><td>U-shape[32]</td><td>PDMS + Resins</td><td>Interlocking</td><td>0–16 N</td><td>20.58 %/N</td><td>5 μm</td><td>86 ms/97 ms</td></tr><tr><td>U-shape (This work)</td><td>PDMS + Resins</td><td>Interlocking</td><td>0–10 N</td><td>65.59 %/N 66.08 %/N</td><td>2.15 μm 2.21 μm</td><td>58 ms/17 ms</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/2c71c134b915603e20fc9cec1bbbcf78f74328ea3fa27668e23f77ac152c806d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/cd287681089e0e2037d6f15ff1327ab4ebac215c0f3fc68807dc301dda008ff7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/22bd6ab498ebd7306a0b5e49e128b88f56a5b5c6c1edb40525d5b6b4714ba04c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/e73ade6b3f19fcb3fbb4453fef897af5578d07a4db61cf112c59dd800385b8e3.jpg)



图11.MNF1与MNF2机械性能对比与校准：(a)响应/恢复时间；(b)增量压力响应曲线；(c)重复性测试。


图10(c)显示，在 $1550 \mathrm{~nm}$ 波长下，相对强度（无压力时的初始输出）的变化与施加的法向力相对应。MNF1在0-1N范围内的压力灵敏度为 $66.08\%$ $\mathrm{N}^{-1}$ ，MNF2为 $65.59\% \mathrm{N}^{-1}$ 。在2-10N范围内，MNF1的灵敏度降至 $3.4\%$ $\mathrm{N}^{-1}$ ，MNF2降至 $2.87\% \mathrm{N}^{-1}$ ，表明两个传感通道具有高度一致性。在不同压力范围内观察到的灵敏度差异可归因于传感器在较大力作用下趋于饱和，导致灵敏度降低。图10(d)展示了两组重复传感单元的压力响应曲线，显示出与MNF1高度接近的相关系数及显著的曲线重叠。

这些结果证实了传感器在整个制造过程中的可靠性和可重复性。为了评估MNF传感器的响应时间和重复性，我们使用了一个法向力计，对传感器表面施加了1N的力。如图11(a)所示，

该传感器表现出卓越的瞬态响应特性，其加载与卸载响应时间分别为84.17 ms和58.37 ms，恢复时间分别为10.02 ms和17.49 ms。此外，恢复时间主要受弹性树脂材料粘度的影响，这是柔性传感器的典型问题。尽管如此，该传感器仍能满足物理刺激实时检测的要求。

当受到逐渐增加的压力水平时，透射光强度逐渐降低，表现出稳定且一致的波动，如图11(b)所示。即使在700次加载和卸载循环后，传感器的输出信号仍保持稳定，未见明显的性能下降，如图11(c)所示。这种耐久性和一致性得益于MNF在PDMS中的稳固封装以及多层传感器结构内的强粘附力。传感器保持了均匀的压力响应，基线强度波动极小，从而有助于


表1 不同形状和封装的MNF传感器对比


<table><tr><td>Shape</td><td>Package Material</td><td>Micro structure</td><td>Force Election range</td><td>Sensitivity</td><td>Diameter</td><td>Response/Recovery Time</td></tr><tr><td>Straight[17]</td><td>PDMS</td><td>None</td><td>0–10 kPa</td><td>1870 kPa-1</td><td>0.8 μm</td><td>10 μs</td></tr><tr><td>Straight[20]</td><td>PDMS + CV</td><td>None</td><td>0–110 kPa</td><td>6.5 % kPa-1</td><td>1.3 μm 2 μm</td><td>110 ms/3s</td></tr><tr><td>U-shape[19]</td><td>PDMS + Capillary</td><td>None</td><td>0–20 N</td><td>0.0108 %/N</td><td>2.7 μm</td><td>&lt;1ms</td></tr><tr><td>U-shape[18]</td><td>PDMS + Resins</td><td>Parallel ring</td><td>0–20 N</td><td>5.4 %/N</td><td>1.2 μm</td><td>-</td></tr><tr><td>U-shape[32]</td><td>PDMS + Resins</td><td>Interlocking</td><td>0–16 N</td><td>20.58 %/N</td><td>5 μm</td><td>86 ms/97 ms</td></tr><tr><td>U-shape (This work)</td><td>PDMS + Resins</td><td>Interlocking</td><td>0–10 N</td><td>65.59 %/N 66.08 %/N</td><td>2.15 μm 2.21 μm</td><td>58 ms/17 ms</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/45d1f5864fbd40d74a40e9898663b277ae9a0542812551703b7a75158a1515ce.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/bcdaebc84544e6348dc67f3a0aa37a0a762209196a3d2e5286a65d21a483e833.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/932f9256f34ced6a65352e0727982c6b43dec28fdb545bb9fd05155ab45b8afd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/daf2cf5e7c678e866de828108d1604a25e0a6cd3b1f5f8c59154385fb5d02eac.jpg)



Fig. 12. (a) Braille recognition Schematic diagram of the experimental setup; (b) "C", "Q", "U", "T", collectively abbreviated as "CQTU" for our institution); (c) intensity spectral response obtained by PST sliding and (d) human finger sliding braille characters.


easy identification of changes in the frequency or amplitude of the output intensity in response to the applied force. The haptic sensor demonstrates excellent sensitivity, durability, and both static and dynamic stability, making it highly suitable for recognizing textured surfaces in robotic applications. Further refinement of the sensor, through reducing the diameter of the MNF and the thickness of the PDMS encapsulating layer, could enhance its tactile pressure sensitivity. 

The sensor developed in this study is compared with a similar type of MNF contact pressure sensor, and the results are presented in Table 1. The data indicate that without a microstructure, achieving high sensitivity necessitates the use of a smaller diameter MNF. However, incorporating a parallel ridge microstructure extends the pressure sensing range effectively (0–20 N), albeit with reduced sensitivity in the low pressure range (0–1 N). The sensitivity within this range is significantly enhanced when an annular ridge microstructure is employed. The MNF sensor proposed here improves sensitivity in the lower pressure range (0–1 N) while also expanding the overall sensing range to 0–10 N by incorporating an interlocking annular ridge microstructure. This sensor is approximately 13 times more effective than the recently reported MNF touch pressure sensors and three times more effective than our previous models. Additionally, the introduction of microstructures effectively amplifies tactile mechanical stimuli, converting them into MNF deformations. Tapering the MNF to 2.2 μm not only boosts sensitivity but also streamlines the fabrication process, enhancing both structural stability and overall elasticity. The designed MNF demonstrates broad application potential for daily robotic grasping tasks within the pressure range of 0–10 N. 

# 3.2. Braille recognition process

Braille is a tactile writing system designed for the visually impaired, characterized by its effective communication through unique textural features. It consists of six dots arranged in a $3 \times 2$ matrix, enabling 64 different combinations that correspond to the 26 English letters. Braille readers interpret these characters by sliding their fingers over the dots to detect and interpret the information. Inspired by this tactile reading process, this paper introduces a braille recognition module using flexible tactile sensing units formed into pair-U-shaped MNFs. This module detects braille characters by sensing subtle geometric changes on the surface and analyzes texture features based on spatial frequency to enhance the sensor's perception of braille features. The experimental setup is depicted in Fig. 12(a), where the sensor is mounted on a glass plate above the braille, which is affixed to a precision electric slider (PST, ZMod-SE-44-10SE) and a Z-axis displacement table (PSD, LZ1000). The upper computer controls the PST to scan the test object, minimizing mechanical vibration interference while regulating speed and pressure. As the displacement table moves, the sensor contacts the raised braille dots, causing bending and changes in the transmission spectrum. These changes are captured by a PD and displayed on an oscilloscope, generating a characteristic waveform. After completing the sliding scan, a column of signals is collected for each channel; from these, two columns of feature signals are extracted to accurately reproduce the braille pattern, with intensity changes corresponding to the positions of the dots in the braille sample. The sensor demonstrated its capability to read four braille characters ("C", "Q", "U", "T", collectively abbreviated as "CQTU" for our institution) to emulate human fingerprint detection capabilities. The velocity-time (v-t) curve illustrates that this sensor type can distinguish between various braille 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/783370b3459a66e1d504b982d2eb1916043d16277378d72c5464e92a8eae66ae.jpg)



Fig. 13. Network model of LSTM.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/d9a9c809ad8b76f16204379850a12e578691e77b9bc0a2e01b6b62ebd2a8d5b8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/8a004456ee5a5663cd7da8abdc23f163d82b8c4bbf63094881ff4d95a8bf4495.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/a7962744788ba2b3ee301b183241dd243592bc76bfce5937f689c4a04d7b7bc3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/c7ddd1689f54ef1d7892b88c2edb2801af741f00e3a64fe61f9f74216d67eebe.jpg)



图12. (a) 盲文识别实验装置示意图；(b) “C”、“Q”、“U”、“T”（合称“CQTU”，代表本机构）；(c) 通过PST滑动获得的强度谱响应；(d) 人手指滑动触摸盲文字符。


易于识别输出强度频率或振幅随施加力变化的情况。该触觉传感器展现出卓越的灵敏度、耐用性以及静态与动态稳定性，使其非常适用于机器人应用中的纹理表面识别。通过减小微纳光纤直径和PDMS封装层厚度对传感器进行进一步优化，可提升其触压灵敏度。

本研究开发的传感器与同类MNF接触压力传感器进行了比较，结果如表1所示。数据显示，若无微结构，实现高灵敏度需采用更小直径的MNF。然而，引入平行脊状微结构能有效扩展压力传感范围（0-20N），尽管在低压区间（0-1N）灵敏度有所降低。当采用环形脊状微结构时，该区间的灵敏度得到显著提升。本文提出的MNF传感器通过引入互锁环形脊状微结构，在提升低压区间（0-1N）灵敏度的同时，将整体传感范围扩展至0-10N。该传感器性能约达近期报道的MNF触压传感器的13倍，亦较我们先前模型提升3倍。此外，微结构的引入有效放大了触觉机械刺激，并将其转化为MNF形变。将MNF锥细至 $2.2\mu \mathrm{m}$ 不仅提升了灵敏度，还简化了制造流程，同时增强了结构稳定性与整体弹性。所设计的MNF在0-10N压力范围内，展现出适用于日常机器人抓取任务的广阔应用前景。

# 3.2. Braille recognition process

盲文是一种专为视障人士设计的触觉书写系统，其特点在于通过独特的纹理特征实现有效沟通。它由六个点按 $3 \times 2$ 矩阵排列，可形成64种不同组合，对应26个英文字母。盲文阅读者通过手指滑过凸点来感知并解读信息。受这种触觉阅读过程的启发，本文提出一种采用成对U形微纳光纤构成的柔性触觉传感单元盲文识别模块。该模块通过感知表面细微的几何变化来检测盲文字符，并基于空间频率分析纹理特征，以增强传感器对盲文特征的感知能力。实验装置如图12(a)所示：传感器安装在覆盖盲文的玻璃板上方，盲文样本固定于精密电动滑台（PST, ZMod-SE-44-10SE）与Z轴位移台（PSD, LZ1000）上。上位机控制PST扫描测试对象，在调节速度与压力的同时最小化机械振动干扰。当位移台移动时，传感器接触凸起的盲文点，引起弯曲及透射光谱变化。这些变化由光电探测器采集并显示于示波器，生成特征波形。完成滑动扫描后，每个通道采集到一列信号；从中提取两列特征信号即可精确复现盲文图案，其强度变化对应盲文样本中凸点的位置。该传感器成功读取了四个盲文字符（“C”“Q”“U”“T”，组合缩写“CQTU”代表本机构），以模拟人类指纹检测能力。速度-时间（ $\{\mathbf{v}^{*}\}-t$ ）曲线表明此类传感器能区分不同盲文

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/6752723997e9310ff32c17c291459a1bac6582036e99492830a4f998feb171ef.jpg)



图13.LSTM的网络模型



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/ac92e472837d2e6eac5bc6344d0de3b7d951497c1bad207ee7c1f50ca62e58a1.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/0c4149c8fbcb4215f6177dea78fd1ca7be0c680701d3735fa29523d44079dcec.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/5f533a689947513066d6ea59f72d20ca3e496837061394443b16736457417962.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/41a08d89c923451f46424afd52632f8e66f4c21ddacbbae6dfbb52168610dd0b.jpg)



Fig. 14. Braille recognition when the tactile sensor is integrated into the human index finger (a) fingertip diagram; (b) braille sliding diagram; (c) Fingertip integrated physical map; (d) Fingertip slide diagram.


characters with different troughs in real-time, as shown in Fig. 12(c). To simulate the tactile experience of visually impaired individuals reading braille, sliding the sensor over a finger to touch the braille yields experimental results comparable to those using the displacement table, as demonstrated in Fig. 12(d). These preliminary tests have confirmed the sensor's effectiveness in recognizing braille characters. 

# 3.3. Intelligent braille recognition in real-time

To further enhance the device's utility, the haptic sensor is integrated with a LSTM algorithm to achieve real-time and effective braille recognition, as illustrated in Fig. 13. LSTM, a variant of Recurrent Neural Networks (RNN), is particularly well-suited for processing sequential data. Designed specifically to overcome the long-term dependency problems of traditional RNNs, LSTM has become the most widely used RNN today. As demonstrated in Fig. 14, the tactile sensor is mounted on a human finger, with the braille affixed to a glass plate. The finger then slides over the braille. Each of the 26 English letters was tested approximately 60 times at various speeds $(0 - 100\mathrm{mm / s})$ and 

pressures $(0 - 4\mathrm{N})$ , totaling 1,619 samples, all of which were input into the LSTM. At present, the recognition of Braille characters usually uses 20 kinds of letters, which is because the features of Braille groups B/K, F/M, G/X, H/U are similar, and the difference is only the time difference between the feature peaks on a certain track. In order to avoid the decline in the recognition accuracy of similar features, we first classified similar letters into one class, with an accuracy of $98.58\%$ , as shown in Fig. 15(a), which proved that our sensor had a good effect. Then we identified 26 individual letters, with an accuracy of $97.10\%$ , as depicted in Fig. 15(b), which showed that our sensor still had an efficient recognition effect on 26 Braille letters. Notably, the recognition accuracy for these grouped letters slightly exceeds that for individual letters. The experimental results confirm that the U-type MNF flexible tactile sensing unit enhances the transmission efficiency of tactile signals during sliding recognition. Additionally, the results validate the efficiency and reliability of the LSTM approach, demonstrating its strong performance in tactile braille recognition for the visually impaired. These findings open new avenues for braille tactile recognition, improve the readability of braille information, and lay a solid foundation for the 


(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/2eb1b1fe8308d51973074f7ae24d625b78250372d78a8fef6ddc1a7f0a5a0a15.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/167fca54b650dc2577b3bde57e7e7ded4c0a5263ab8cb006fc26cf6b952c4afd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/55ca2b2fca4617cccda1161743f8f4e6ec038f572af1651720d0ebfbd454596a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/fc594534064cd1ecd299dc27d79db8bf49a54cd73ba924d1baa338f3f1fab5c4.jpg)



图14.触觉传感器集成于人体食指时的盲文识别(a)指尖示意图；(b)盲文滑动示意图；(c)指尖集成实物图；(d)指尖滑动示意图。


如图12(c)所示，传感器能够实时识别具有不同凹陷特征的盲文字符。为模拟视障人士触摸盲文的触觉体验，将传感器滑过手指接触盲文点，所得实验结果与使用位移台的情况相当，如图12(d)所示。这些初步测试已证实该传感器在识别盲文字符方面的有效性。

# 3.3. Intelligent braille recognition in real-time

为进一步提升设备的实用性，该触觉传感器与LSTM算法相结合，实现了实时高效的盲文识别，如图13所示。LSTM作为循环神经网络（RNN）的一种变体，特别适合处理序列数据。它专为克服传统RNN的长期依赖问题而设计，已成为目前应用最广泛的RNN模型。如图14所示，触觉传感器安装在人类手指上，盲文样本固定于玻璃板表面。手指在盲文上滑动进行检测。每个英文字母（共26个）在不同速度（0-100 mm/s）下各测试约60次，

压力（0-4N），共计1619个样本，全部输入LSTM。目前，盲文字符的识别通常使用20种字母，这是因为盲文组B/K、F/M、G/X、H/U的特征相似，差异仅在于特定轨迹上特征峰的时间差。为避免相似特征导致识别准确率下降，我们首先将相似字母归为一类，准确率达到 $98.58\%$ ，如图15(a)所示，这证明我们的传感器具有良好的效果。随后，我们识别了26个独立字母，准确率为 $97.10\%$ ，如图15(b)所示，这表明我们的传感器对26个盲文字母仍具有高效的识别效果。值得注意的是，这些分组字母的识别准确率略高于独立字母。实验结果证实，U型MNF柔性触觉传感单元提升了滑动识别过程中触觉信号的传输效率。此外，结果验证了LSTM方法的效率和可靠性，展示了其在视障者触觉盲文识别中的强大性能。这些发现为盲文触觉识别开辟了新途径，提高了盲文信息的可读性，并为相关应用奠定了坚实基础。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/278a220632e236f3d638887c89ec685409ccc404dfbe478b60efa4d01b0c72c0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/f8d0088299f2abd8072736d50335966076c38abaf603c4bc41b309ce2733af54.jpg)



Fig. 15. (a) Recognition rate for 22 groups of letters; (b) Recognition rate for 26 groups of letters.



Table 2 Comparison of scanning methods for different types of sensors.


<table><tr><td>Type</td><td>Scanning Number</td><td>Signal characteristics</td><td>Machine learning</td><td>Number of Characters</td><td>Recognition rate</td></tr><tr><td>Piezoresistive [7]</td><td>1</td><td>Superposition</td><td>NO</td><td>-</td><td>-</td></tr><tr><td>Piezoresistive [8]</td><td>3</td><td>Counterparts</td><td>NO</td><td>-</td><td>-</td></tr><tr><td>Piezoresistive&amp; Piezoelectric [6]</td><td>1</td><td>Segmentation Superposition</td><td>CNN-LSTM</td><td>20</td><td>84.2 %</td></tr><tr><td>MNF (This work)</td><td>1</td><td>Counterparts</td><td>LSTM</td><td>22</td><td>98.58 %</td></tr><tr><td></td><td></td><td></td><td></td><td>26</td><td>97.10 %</td></tr></table>

development of more intelligent and efficient braille recognition systems in the future. 

The proposed sensor is compared with other surface texture touch pressure sensors, as detailed in Table 2. The results indicate that flexible electronic haptic sensors cannot achieve one-to-one feature signal detection in a single slide. The recently reported piezoresistive-piezoelectric dual-mode sensor [6] requires segmentation first due to signal overlap, and even the combined CNN-LSTM algorithm fails to achieve high accuracy. In contrast, the braille sensor introduced in this study captures the corresponding characteristic peaks with a single slide, reaching an ideal state. Compared with traditional tactile recognition methods for visually impaired individuals, the method proposed here not only enhances efficiency but also serves as a valuable reference and source of inspiration for future research and practical applications. 

# 4. Conclusion

In this study, we introduce a pair-U-shaped MNF tactile sensor designed for braille recognition. Inspired by the tactile skin structure of human fingers, we propose a bionic design that effectively increases the sensor's surface roughness, enhancing its ability to detect mechanical stimuli from sliding or friction. Comprehensive performance tests reveal that the sensor can accurately detect forces ranging from 0 to $10\mathrm{N}$ and maintains dual-channel consistency. Specifically, within the $0 - 1\mathrm{N}$ range, the sensor demonstrates a force sensing sensitivity with response/ recovery times of 84.17/10.02 ms and 58.37/17.49 ms, respectively, and achieves sensitivity rates of $66.08\% \mathrm{N}^{-1}$ and $65.59\% \mathrm{N}^{-1}$ . It also exhibits strong anti-interference capabilities. Utilizing LSTM machine learning, the sensor successfully identifies 26 English letters with 97.10 % accuracy under varying intensities and speeds of slides. By grouping four sets of letters with similar characteristics, the accuracy rate 

increases to $98.58\%$ . This showcases its significant potential as a fiber optic tactile recognition tool. To enhance braille recognition accuracy further, the LSTM model could be optimized or combined with other models. The innovative MNF flexible tactile sensing technology developed in this study has broad application prospects, including robot-assisted reading, surface detection, surgical treatments, and robotic fingertip sensing. This groundbreaking research establishes a solid foundation for advancing intelligent technologies and improving human-computer interactions, offering more convenient, safe, and innovative solutions for society's future. 

# Funding

This work was supported in part by Chongqing Natural Science Fund Innovation and Development Joint fund under Grant CSTB2023NSCQ-LZX0008, in part by the Chongqing Talents Program under Grant CSTC2021YCJH-BGZXM0128, in part by Chongqing University of Technology Research and Innovation Team Cultivation Program under Grant 2023TDZ002, in part by the Graduate Student Innovation Program of Chongqing University of Technology under Grant gzlcx20243090. 

# CRediT authorship contribution statement

Ling Huang: Writing - original draft, Project administration, Methodology, Formal analysis, Data curation. Binbin Luo: Conceptualization. Xue Zou: Resources. Decao Wu: Investigation. Fudan Chen: Resources. Zhihai Liu: Validation. Mingfu Zhao: Project administration. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/0bc17febbfdb61a5b3bb8aaca5003dc805213a7a42001bd4eb7fbb4bd3400697.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/59d5a9d2-cd20-48b0-bcde-bb1dc76b33d2/ef7cf6c62cdddc460e351834873fde9858ee7b876fcec154bc77c8d88da54e4e.jpg)



图15. (a) 22组字母的识别率；(b) 26组字母的识别率。



表2不同类型传感器的扫描方法比较


<table><tr><td>Type</td><td>Scanning Number</td><td>Signal characteristics</td><td>Machine learning</td><td>Number of Characters</td><td>Recognition rate</td></tr><tr><td>Piezoresistive [7]</td><td>1</td><td>Superposition</td><td>NO</td><td>-</td><td>-</td></tr><tr><td>Piezoresistive [8]</td><td>3</td><td>Counterparts</td><td>NO</td><td>-</td><td>-</td></tr><tr><td>Piezoresistive&amp; Piezoelectric [6]</td><td>1</td><td>Segmentation Superposition</td><td>CNN-LSTM</td><td>20</td><td>84.2 %</td></tr><tr><td>MNF (This work)</td><td>1</td><td>Counterparts</td><td>LSTM</td><td>22</td><td>98.58 %</td></tr><tr><td></td><td></td><td></td><td></td><td>26</td><td>97.10 %</td></tr></table>

未来开发更智能、高效的盲文识别系统。

所提出的传感器与其他表面纹理触压传感器进行了比较，详见表2。结果表明，柔性电子触觉传感器无法在单次滑动中实现一对一特征信号检测。近期报道的压阻-压电双模传感器[6]因信号重叠需先进行分割处理，即使结合CNN-LSTM算法仍难以实现高精度。相比之下，本研究引入的盲文传感器通过单次滑动即可捕捉对应特征峰，达到理想状态。与传统的视障人士触觉识别方法相比，本文提出的方法不仅提升了效率，也为未来研究和实际应用提供了有价值的参考与启示。

# 4.结论

在本研究中，我们介绍了一种专为盲文识别设计的U型对结构MNF触觉传感器。受人类手指触觉皮肤结构的启发，我们提出了一种仿生设计，有效增加了传感器表面粗糙度，从而提升了其检测滑动或摩擦产生的机械刺激的能力。综合性能测试表明，该传感器能精确检测0至10N范围内的力，并保持双通道一致性。具体而言，在0-1N范围内，传感器表现出力感测灵敏度，响应/恢复时间分别为84.17/10.02 ms和58.37/17.49 ms，灵敏度达到 $66.08\% \mathrm{N}^{-1}$ 和 $65.59\% \mathrm{N}^{-1}$ 。它还展现出强大的抗干扰能力。利用LSTM机器学习，传感器在不同滑动强度和速度下成功识别了26个英文字母，准确率达 $97.10\%$ 。通过将四组特征相似的字母分组，准确率

提升至 $98.58\%$ 。这彰显了其作为光纤触觉识别工具的巨大潜力。为进一步提高盲文识别准确率，可对LSTM模型进行优化或与其他模型结合。本研究开发的创新MNF柔性触觉传感技术具有广阔的应用前景，涵盖机器人辅助阅读、表面检测、手术治疗及机器人指尖传感等领域。这项突破性研究为推进智能技术、改善人机交互奠定了坚实基础，为社会未来提供了更便捷、安全且创新的解决方案。

# 资金

本研究部分得到重庆市自然科学基金创新发展联合基金（项目编号：CSTB2023NSCQ-LZX0008）、部分得到重庆市英才计划（项目编号：CSTC2021YCJH-BGZXM0128）、部分得到重庆理工大学科研创新团队培育计划（项目编号：2023TDZ002）、部分得到重庆理工大学研究生创新计划（项目编号：gzlcx20243090）的资助。

# CRediT作者贡献声明

黄玲：撰写——初稿，项目管理，方法论，形式分析，数据管理。罗彬彬：概念化。邹雪：资源。吴德操：调查。陈福丹：资源。刘志海：验证。赵明福：项目管理。

# Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# Data availability

No data was used for the research described in the article. 

# References



[1] G.B. Holanda, J.W.M. Souza, D.A. Lima, L.B. Marinho, A.M. Girão, J.B. Bezerra Frota, P.P. Rebouças Filho, Development of OCR system on android platforms to aid reading with a refreshable braille display in real time, Measurement 120 (2018) 150-168, https://doi.org/10.1016/jmeasurement.2018.02.021. 





[2] J.M.B. Jacqueline R, A.M. Patricia, et al., The Lancet Global Health Commission on Global Eye Health: vision beyond 2020, The Lancet Global Health 9 (4) (2021) e489-e551. 





[3] Asebriy Z, Raghay S, Bencharef O. An Assistive Technology for Braille Users to Support Mathematical Learning: A Semantic Retrieval System[J]. Symmetry, 2018,10(11):547-547. https://doi.org/10.3390/sym10110547. 





[4] M.A. Darden, C.J. Schwartz, Skin tribology phenomena associated with reading braille print: The influence of cell patterns and skin behavior on coefficient of friction, Wear 332-333 (2015) 734-741, https://doi.org/10.1016/j.wear.2014.12.053. 





[5] H. Niu, S. Gao, W. Yue, Y. Li, W. Zhou, H. Liu, Highly Morphology-Controllable and Highly Sensitive Capacitive Tactile Sensor Based on Epidermis-Dermis-Inspired Interlocked Asymmetric-Nanocone Arrays for Detection of Tiny Pressure, Small 16 (2020) 1904774, https://doi.org/10.1002/smll.201904774. 





[6] Z. Gao, L. Chang, B. Ren, J. Han, J. Li, Enhanced braille recognition based on piezoresistive and piezoelectric dual-mode tactile sensors, Sensors and Actuators a: Physical 366 (2024) 115000, https://doi.org/10.1016/j.sna.2023.115000. 





[7] Cao, Y., Li, T., Gu, Y., Luo, H., Wang, S., Zhang, T., 2018. Fingerprint-Inspired Flexible Tactile Sensor for Accurately Discerning Surface Texture. Small 14, 1703902. https://doi.org/10.1002/smll.201703902. 





[8] X. Tang, W. Yang, S. Yin, G. Tai, M. Su, J. Yang, H. Shi, D. Wei, Yang, Controllable Graphene Wrinkle for a High-Performance Flexible Pressure Sensor, ACS Appl. Mater. Interfaces 13 (Jun 2021) 20448–20458, https://doi.org/10.1021/acsami.0c22784. 





[9] Z. Zhu, Y. Xu, W. Lin, Z. Hu, Z. Lin, Z. Sun, Z. Peng, Z. Wang, Robust and Flexible Sliding Tactile Sensor for Surface Pattern Perception and Recognition, Advanced Intelligent Systems 5 (2023) 2300225, https://doi.org/10.1002/aisy.202300225. 





[10] X.-F. Zhao, C.-Z. Hang, H.-L. Lu, K. Xu, H. Zhang, F. Yang, R.-G. Ma, J.-C. Wang, D. W. Zhang, A skin-like sensor for intelligent Braille recognition, Nano Energy 68 (2020) 104346, https://doi.org/10.1016/j.nanoen.2019.104346. 





[11] S. Stassi, V. Cauda, G. Canavese, C. Pirri, Flexible Tactile Sensing Based on Piezoresistive Composites: A Review, Sensors 14 (2014) 5296-5332, https://doi.org/10.3390/s140305296. 





[12] J. Qin, L. Yin, Y. Hao, S. Zhong, D. Zhang, K. Bi, Y. Zhang, Y. Zhao, Z. Dang, Flexible and Stretchable Capacitive Sensors with Different Microstructures, Advanced Materials 33 (2021) 2008267, https://doi.org/10.1002/adma.202008267. 





[13] Y. Pang, X. Xu, S. Chen, Y. Fang, X. Shi, Y. Deng, Z.-L. Wang, C. Cao, Skin-inspired textile-based tactile sensors enable multifunctional sensing of wearables and soft robots, Nano Energy 96 (2022) 107137, https://doi.org/10.1016/j.nanoen.2022.107137. 





[14] X. Qu, J. Xue, Y. Liu, W. Rao, Z. Liu, Z. Li, Fingerprint-shaped triboelectric tactile sensor, Nano Energy 98 (2022) 107324, https://doi.org/10.1016/j.nanoen.2022.107324. 





[15] D. Lu, T. Liu, X. Meng, B. Luo, J. Yuan, Y. Liu, S. Zhang, C. Cai, C. Gao, J. Wang, S. Wang, S. Nie, Wearable Triboelectric Visual Sensors for Tactile Perception, Advanced Materials 35 (2023) 2209117, https://doi.org/10.1002/adma.202209117. 





[16] Yao, N., Wang, X., Ma, S., Song, X., Wang, Shan, Shi, Z., Pan, J., Wang, Shipeng, Xiao, J., Liu, H., Yu, L., Tang, Y., Zhang, Z., Li, X., Fang, W., Zhang, L., Tong, L., 2022. Single optical microfiber enabled tactile sensor for simultaneous temperature and pressure measurement. Photon. Res. 10, 2040. https://doi.org/10.1364/PRJ.461182. 





[17] L. Zhang, J. Pan, Z. Zhang, H. Wu, N. Yao, D. Cai, Y. Xu, J. Zhang, G. Sun, L. Wang, W. Geng, W. Jin, W. Fang, D. Di, L. Tong, Ultrasensitive skin-like wearable optical sensors based on glass micro/nanofibers, Opto-Electronic Advances 3 (2020) 19002201-19002207, https://doi.org/10.29026/oea.2020.190022. 





[18] C. Jiang, Z. Zhang, J. Pan, Y. Wang, L. Zhang, L. Tong, Finger-Skin-Inspired Flexible Optical Sensor for Force Sensing and Slip Detection in Robotic Grasping, 





Adv Materials Technologies 6 (2021) 2100285, https://doi.org/10.1002/admt.202100285. 





[19] Y. Tang, H. Liu, J. Pan, Z. Zhang, Y. Xu, N. Yao, L. Zhang, L. Tong, Optical Micro/Nanofiber-Enabled Compact Tactile Sensor for Hardness Discrimination, ACS Appl. Mater. Interfaces 13 (2021) 4560–4566, https://doi.org/10.1021/acsami.0c20392. 





[20] H. Liu, X. Song, X. Wang, S. Wang, N. Yao, X. Li, W. Fang, L. Tong, L. Zhang, Optical Microfibers for Sensing Proximity and Contact in Human-Machine Interfaces, ACS Appl. Mater. Interfaces 14 (2022) 14447-14454, https://doi.org/10.1021/acsami.1c23716. 





[21] Li, L., Sheng, S., Liu, Y., Wen, J., Song, C., Chen, Z., Xu, W., Zhang, Z., Fan, W., Chen, C., Sun, Q., Shum, P.-P., 2023. Automatic and continuous blood pressure monitoring via an optical-fiber-sensor-assisted smartwatch. PhotoniX 4, 21. https://doi.org/10.1186/s43074-023-00099-z. 





[22] L. Hou, T. Jiang, T. Yu, C. Cao, X. Tu, J. Zhang, J. Pan, S. Wang, N. Zhou, N. Yao, L. Zhang, Tapered Optical Fiber Enabled Distributed Sensors with High Spatial Resolution by Deep Learning, Advanced Optical Materials (2024) 2303118, https://doi.org/10.1002/adom.202303118. 





[23] S. Wang, X. Wang, S. Wang, W. Yu, L. Yu, L. Hou, Y. Tang, Z. Zhang, N. Yao, C. Cao, H. Dong, L. Zhang, H. Bao, Optical-Nanofiber-Enabled Gesture-Recognition Wristband for Human-Machine Interaction with the Assistance of Machine Learning, Advanced Intelligent Systems 5 (2023) 2200412, https://doi.org/10.1002/aisy.202200412. 





[24] N. Bai, Y. Xue, S. Chen, L. Shi, J. Shi, Y. Zhang, X. Hou, Y. Cheng, K. Huang, W. Wang, J. Zhang, Y. Liu, C.F. Guo, A robotic sensory system with high spatiotemporal resolution for texture recognition, Nat Commun 14 (2023) 7121, https://doi.org/10.1038/s41467-023-42722-4. 





[25] X. Zhi, S. Ma, Y. Xia, B. Yang, S. Zhang, K. Liu, M. Li, S. Li, W. Peiyuan, X. Wang, Hybrid tactile sensor array for pressure sensing and tactile pattern recognition, Nano Energy 125 (2024) 109532, https://doi.org/10.1016/j.nanoen.2024.109532. 





[26] S.-M. Chang, S. Hur, J. Park, D.-G. Lee, J. Shin, H.S. Kim, S.E. Song, J.M. Baik, M. Kim, H.-C. Song, C.-Y. Kang, Optimization of piezoelectric polymer composites and 3D printing parameters for flexible tactile sensors, Additive Manufacturing 67 (2023) 103470, https://doi.org/10.1016/j.addma.2023.103470. 





[27] Zhang, G., Wu, X., Ge, Q., Li, S., Zhang, W., Shi, J., Gui, L., Yu, B., 2020. Axial strain applied in-in fiber Mach-Zehnder interferometer for acceleration measurement. Opt. Express 28, 18596. https://doi.org/10.1364/OE.391235. 





[28] L. Tong, J. Lou, Mazur E. Single-mode guiding properties of subwavelength-diameter silica and silicon wire waveguides[J]. Optics Express, (2004), 12(6):1025-1035. https://doi.org/10.1364/OPEX.12.001025. 





[29] K. Liu, J. Fan, B. Luo, et al., Highly sensitive vibration sensor based on the dispersion turning point microfiber Mach-Zehnder interferometer, Optics Express 29 (21) (2021) 32983-32995, https://doi.org/10.1364/OE.439959. 





[30] L. Tong, M. Sumetsky, Subwavelength and nanometer diameter optical fibers, Springer Science & Business Media (2011), https://doi.org/10.1007/978-3-642-03362-9. 





[31] X. Zhang, M. Belal, G.Y. Chen, Z. Song, G. Brambilla, T.P. Newson, Compact optical microfiber phase modulator, Opt. Lett. 37 (2012) 320, https://doi.org/10.1364/OL.37.000320. 





[32] C. Fan, B. Luo, et al., Research on flexible bionic microstructured tactile sensors based on micro-nano optical fibre, Acta Sinaca China 43 (21) (2023) 67-77, https://doi.org/10.3788/aos231313. 



Ling Huang received the B.S. degree in Communication Engineering from Fujian Normal University, Fujian, in 2021 She is currently pursuing the M.S. degree at Chongqing University of Technology. Her current research interests include smart sensing technology and engineering applications. 

Binbin Luo is currently a Professor at Chongqing University of Technology, Chongqing, China, and he is a member of Optica. He completed his Ph.D. and master in optical engineering at University of Electronic Science and Technology of China, China. His research group focuses on developing the principle of optical fiber sensor and its application in intelligent structural engineering and biomedical fields, and he has published more than 60 research papers in these fields. 

Xue Zou is currently a lecturer with Chongqing University of Technology, Chongqing, China. She received the master's degree from Chongqing University, China. And She is working on his Ph.D. degree at Chongqing University of Posts and Telecommunications, China. Her current research focuses on optical fiber intelligent sensors. 

Decao Wu is currently an associated Professor at Chongqing University of Technology, Chongqing, China. He completed his Ph.D. in optical engineering at the Chongqing University, China. He focuses on optical fiber sensor, Infrared laser detection technology and their application in intelligent structural engineering and biomedical fields, and he has published more than 15 research papers in these fields. 

# 利益冲突声明

作者声明，对于本论文所报告的工作，不存在任何已知的可能影响研究结果的竞争性经济利益或个人关系。

# 数据可用性

本文所述研究未使用任何数据。

# 参考文献

[1] G.B. Holanda, J.W.M. Souza, D.A. Lima, L.B. Marinho, A.M. Girao, J.B. Bezerra Frota, P.P. Rebouças Filho, 用于辅助盲文点显器实时阅读的安卓平台OCR系统开发，Measurement 120 (2018) 150-168, https://doi.org/10.1016/jmeasurement.2018.02.021。[2] J.M.B. Jacqueline R, A. M. Patricia, 等，《柳叶刀-全球健康》全球眼健康委员会：2020年之后的愿景，The Lancet Global Health 9 (4) (2021) e489-e551。[3] Asebriy Z, Raghay S, Bencharef O.一种辅助盲文用户支持教学学习的辅助技术：语义检索系统[J]. Symmetry, 2018, 10(11):547-547. https://doi.org/10.3390/sym10110547。[4] M.A. Darden, C.J. Schwartz, 阅读盲文时相关的皮肤摩擦学现象：单元图案和皮肤行为对摩擦系数的影响，Wear 332-333 (2015) 734-741, https://doi.org/10.1016/j.wear.2014.12.053。[5] H. Niu, S. Gao, W. Yue, Y. Li, W. Zhou, H. Liu, 基于表皮-真皮仿生互锁不对称纳米锥阵列的高度形貌可控且高灵敏电容式触觉传感器，用于微小压力检测，Small 16 (2020) 1904774, https://doi.org/10.1002/smll.201904774。[6] Z. Gao, L. Chang, B. Ren, J. Han, J. Li, 基于压阻和压电双模式触觉传感器的增强型盲文识别，Sensors and Actuators a: Physical 366 (2024) 115000, https://doi.org/10.1016/j.sna.2023.115000。[7] Cao, Y., Li, T., Gu, Y., Luo, H., Wang, S., Zhang, T., 2018. 受指纹启发的柔性触觉传感器，用于精确辨别表面纹理。Small 14, 1703902. https://doi.org/10.1002/smll.201703902。[8] X. Tang, W. Yang, S. Yin, G. Tai, M. Su, J. Yang, H. Shi, D. Wei, Yang, 用于高性能柔性压力传感器的可控石墨烯褶皱，ACS Appl. Mater. Interfaces 13 (Jun 2021) 20448-20458, https://doi.org/10.1021/acsa mi.0c22784。[9] Z. Zhu, Y. Xu, W. Lin, Z. Hu, Z. Lin, Z. Sun, Z. Peng, Z. Wang, 用于表面图案感知与识别的鲁棒柔性滑动触觉传感器，Advanced Intelligent Systems 5 (2023) 2300225, https://doi.org/10.1002/aisy.202300225。[10] X.-F. Zhao, C.-Z. Hang, H.-L. Lu, K. Xu, H. Zhang, F. Yang, R.-G. Ma, J.-C. Wang, D.W. Zhang, 一种用于智能盲文识别的类皮肤传感器，Nano Energy 68 (2020) 104346, https://doi.org/10.1016/j.nanoen.2019.104346。[11] S. Stassi, V. Cauda, G.Canavese, C.Pirri, 基于压阻复合材料的柔性触觉传感：综述，Sensors 14 (2014) 5296-53 32, https://doi.org/10.3390/s140305296。[12] J.Qin,L.Yin,Y.Hao,S.Zhong,D.Zhang,K.Bi Y.Zhang,Y.Zhao,Z.Dang具有不同微结构的柔性和可拉伸电容传感器，Advanced Materials 33 (2021) 2008267, https://doi.org/10.1002/adma.202008267。[13] Y.Pang,X.Xu,S.ChenY.FangX.ShiY.DengZ.-L.Wang,C.Cao受皮肤启发的基于纺织品的触觉传感器实现可穿戴设备和软机器人的多功能传感，Nano Energy 96 (2022) 107137, https://doi.org/10.1016/j.nanoen.2022.107137。[14] X.Qu,J.Xue,Y.Liu,W.RaoZ.LiuZ.Li指纹状摩擦电触觉传感器，Nano Energy 98 (2022) 107324, https://doi.org/10.1016/j.nanoen.2022.107324。[15] D.Lu T.LiuX.MengB.LuoJ.YuanY.LiuS.ZhangC.CaiC.GaoJ.WangS.WangS.Nie用于触觉感知的可穿戴摩擦电视感觉传感器，Advanced Materials 35 (2023) 2209117,https://doi.org/10.1002/adma.202209117。[16] Yao,N.WangX.Ma,S.SongX.WangShanShiZ.PanJ.WangShipengXiaoJ.LiuH.YuL.TangY.ZhangZ.LiX.FangW.ZhangL.T ongL., 2022单根光学微纤维实现的触觉传感器用于同时测量温度和压力。Photon.Res. 10, 2040. https://doi.org/10.1364/PRJ.461182。[17] L.ZhangJ.PanZ.ZhangH.WuN.YaoD.C aiY.XuJ.ZhangG.SunL.WangW.GengW.JinW.FangD.DiL.Tong基于玻璃微/纳米纤维的超灵敏类皮肤可穿戴光学传感器，Opto-Electronic Advances 3 (2020) 19002201-19 002207，https://doi.org/10.29026/oea.2020.190022。[18] C.JiangZ.ZhangJ.PanY.WangL.ZhangL.Tong受手指皮肤启发的柔性光学传感器，用于机器人抓取中的力传感和滑动检测，

Adv Materials Technologies 6 (2021) 2100285, https://doi.org/10.1002/admt.202100285. [19] 唐勇，刘浩，潘俊，张振，徐洋，姚纳新，张磊，童利民，用于硬度辨别的光学微纳米纤维紧凑型触觉传感器，ACS Appl. Mater. Interfaces 13 (2021) 4560-4566, https://doi.org/10.1021/acsam i.oC20392. [20] 刘浩，宋晓，王鑫，王帅，姚纳新，李雪，方伟，童利民，张磊，用于人机界面接近与接触传感的光学微纤维，ACS Appl. Mater. Interfaces 14 (2022) 14447-14454, https://doi.org/10.1021/acsami.lc23716. [21] 李林，盛帅，刘洋，文静，宋超，陈哲，徐伟，张振，范伟，陈晨，孙琪，舒鹏飞，2023. 通过光纤传感器辅助智能手表实现自动连续血压监测. PhotoniX 4, 21. https:// doi.org/10.1186/s43074-023-00099-z. [22] 侯磊，姜涛，于涛，曹晨，涂晓，张杰，潘俊，王帅，周宁，姚纳新，张磊，基于深度学习的锥形光纤实现高空间分辨率分布式传感，Advanced Optical M aterials (2024) 2303118, https://doi.org/10.1002/adom.202303118. [23] 王帅，王鑫，王帅，余伟，余磊，侯磊，唐勇，张振，姚纳新，曹晨，董浩，张磊，鲍华，基于光学纳米纤维和机器学习辅助的手势识别腕带用于人机交互，Advanced Intelligent Systems 5 (2023) 2200412, https://doi.org/10.1002/aisy.202200412. [24] 白宁，薛宇，陈帅，石磊，石健，张宇，侯鑫，程宇，黄凯，王伟，张杰，刘洋，郭传飞，一种用于纹理识别的高时空分辨率机器人传感系统, Nat Commun 14 (2023) 7 121, https://doi.org/10.1038/s41467-023-42722-4. [25] 智鑫，马帅，夏宇，杨波，张帅，刘凯，李明，李帅，王培元，王鑫，用于压力传感和触觉模式识别的混合触觉传感器阵列, Nano Energy 12 5 (2024) 109532, https://doi.org/10.1016/j.nanoen.2024.109532. [26] 张世明, 许世, 朴俊, 李大根申俊金洪锡宋尚恩白俊模金敏宋铉哲姜昌郁柔性触觉传感器用压电聚合物复合材料及3D打印参数的优化Additive Manufacturing 67 (2023) 103470, https://doi.org/10.1016/j.ad ma.2023.103470. [27] 张国, 吴鑫, 葛强, 李帅, 张伟, 石健, 桂磊, 于波, 2020. 用于加速度测量的光纤内马赫-曾德尔干涉仪轴向应变应用.Opt.Express 28, 18596. https://doi.org/10.1364/O E.391235. [28] 童利民娄军Mazur E.A波长直径硅和硅线波导的单模导波特性[J].Optics Express,(2004), 12(6):1025-1035. https://doi.org/10.1364/OPEX.12.001025. [29] 刘凯, 范俊, 罗斌等, 基于色散转折点微纤维马赫-曾德尔干涉仪的高灵敏度振动传感器, Optics Express 29 (21) (2021) 32983-32995, https://doi.org/10.1364/OE.439959. [30] 童利民,Sumetsky M.,亚波长及纳米直径光学纤维,Springer Science & Business Media (2011), https://doi.org/10.1007/978 -3-642-03362-9. [31] 张鑫,Belal M.,陈国英,宋振,Brambilla G.,Newson T.P.,紧凑型光学微纤维相位调制器,Opt.Lett.37 (2012) 320,https://doi.org/10.1364/OL.37.000320. [32] 范超,罗斌等,基于微纳光纤的柔性仿生微结构触觉传感器研究,中国光学学报 43 (21) (2023) 67-77 ,https://doi.org/10.3788/aoaes231313

黄玲于2021年在福建师范大学获得通信工程学士学位。目前，她正在重庆理工大学攻读硕士学位。她的当前研究方向包括智能传感技术及其工程应用。

罗彬彬现任中国重庆理工大学教授，也是美国光学学会（Optica）会员。他在中国电子科技大学获得光学工程专业硕士和博士学位。其研究团队致力于光纤传感原理及其在智能结构工程与生物医学领域的应用研究，已在这些领域发表60余篇学术论文。

邹雪目前是中国重庆重庆理工大学的讲师。她在中国重庆大学获得硕士学位，并正在中国重庆邮电大学攻读博士学位。她目前的研究聚焦于光纤智能传感器。

吴德操目前是中国重庆重庆理工大学的副教授。他在中国重庆大学获得光学工程博士学位。他的研究聚焦于光纤传感器、红外激光探测技术及其在智能结构工程和生物医学领域的应用，并在这些领域发表了超过15篇研究论文。

Fudan Chen received the B.S. degree in Electronic Information Engineering from Xidian University, Xi'an, in 2022. He is currently pursuing the master's degree in electronic Information from Chongqing University of Technology. His research focuses on optical fiber wearable sensor. 

Zhihai Liu is currently studying for a bachelor's degree in electronic information at Chongqing University of Technology. His research interest focuses on Intelligent Sensing Technology and Engineering Applications. 

Mingfu Zhao received the M.S. degrees from Xi an Jiaotong University, Chengdu, and the Ph.D. degrees from Chongqing University of Technology, Chongqing, China. He is currently a professor at the School of Electrical and Electronic Engineering at Chongqing University of Technology. His research focuses on optical fiber sensor and photoelectric detection technology, and he has published more than 80 research papers in these fields 

陈复旦于2022年在西安电子科技大学获得电子信息工程学士学位。目前，他正在重庆理工大学攻读电子信息硕士学位。他的研究主要集中在光纤可穿戴传感器领域。

刘志海目前就读于重庆理工大学电子信息专业，攻读学士学位。他的研究兴趣主要集中在智能传感技术及其工程应用。

赵明福分别于西安交通大学（成都）获得硕士学位，于重庆理工大学获得博士学位。他目前是重庆理工大学电气与电子工程学院的教授。他的研究主要集中在光纤传感器和光电检测技术领域，并在这些领域发表了80多篇研究论文。