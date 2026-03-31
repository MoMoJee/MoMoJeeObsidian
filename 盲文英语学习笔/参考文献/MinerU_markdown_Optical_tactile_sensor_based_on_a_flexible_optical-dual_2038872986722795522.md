# Optical tactile sensor based on a flexible optical fiber ring resonator for intelligent braille recognition

HENG WANG,1 LIN MA,1 QIN NIE,1 XUEHAO HU,2 $\textcircled{1}$ XIAOLI LI,3,4 RUI MIN,3,4 AND ZHUO WANG5,* 

1College of Science, Shenyang Aerospace University, Shenyang 110136, China 

2Department of Electromagnetism and Telecommunication, University of Mons, 7000 Mons, Belgium 

3Department of Psychology, Faculty of Arts and Sciences, Beijing Normal University, Zhuhai 519087, China 

4Faculty of Psychology, Beijing Normal University, Beijing 100875, China 

5Department of Physics, Faculty of Arts and Sciences, Beijing Normal University, Zhuhai 519087, China *zhuowang@bnu.edu.cn 

Abstract: Inspired by human skin, bionic tactile sensing is effectively promoting development and innovation in many fields with its flexible and efficient perception capabilities. Optical fiber, with its ability to perceive and transmit information and its flexible characteristics, is considered a promising solution in the field of tactile bionics. In this work, one optical fiber tactile sensing system based on a flexible PDMS-embedded optical fiber ring resonator (FRR) is designed for braille recognition, and the Pound-Drever-Hall (PDH) demodulation scheme is adopted to improve the detection sensitivity. Theoretical simulations and experimental verifications show that by adopting a bionic sliding approach and a Multilayer Perceptron Neural Network, a single FRR with a hardness gradient design can detect eight different tactile pressures in braille characters with an accuracy of $9 8 . 5 7 \%$ . Furthermore, after training and testing, the MLP-LSTM model classifies time series signals, thereby achieving completely accurate encoding of braille keywords and braille poems. The advantages of the optical fiber tactile sensing system in this study are that the high-quality factor FRR can detect subtle differences in braille dots, it is not affected by changes in optical power due to its relies on PDH frequency demodulation, and the application of machine learning algorithms can enhance the robustness to slight pressure errors and simplify the recognition process. This solution opens up what we believe is a new optical approach for bionic tactile perception and has important potential value in promoting human-computer interaction, smart medical care, and other fields. 

$\circledcirc$ 2025 Optica Publishing Group under the terms of the Optica Open Access Publishing Agreement 

# 1. Introduction

The human tactile perception system is a complex network of specialized cells, nerves, and brain regions that allow us to feel and perceive the world around us. It plays a crucial role in everyday activities, from picking up delicate objects to navigating our environment in the dark [1]. Tactile sensing encompasses many critical applications, including intelligent robots, biomimetic prosthetics, remote surgery, and human-machine interfaces (HMI) [2–4]. Tactile pressure sensors are crucial components of intelligent robots. Detecting pressure is particularly important as it enables robots to perceive, grasp, and hold objects, and increasing the sensitivity of these sensors enhances their performance in these tasks [5,6]. Moreover, the biological haptic perception of the human fingertip involves identifying and recognizing objects and surface textures, which requires high spatial resolution in sensor structures and fast response to subtly changing dynamic pressure [7,8]. In the fields of life health and auxiliary medicine, tactile perception also plays 

# 基于柔性光纤环形谐振器的光学触觉传感器用于智能盲文识别

王恒，1 林马，1 聂琴，1 胡学浩，2 李晓丽，3,4 闵瑞，3,4 与王卓5,*

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/331f0a11a54763543804ade4f91d1f24e3fe969043a97102b396d3ff87ea25ce.jpg)




1College of Science, Shenyang Aerospace University, Shenyang 110136, China 





2Department of Electromagnetism and Telecommunication, University of Mons, 7000 Mons, Belgium 





3Department of Psychology, Faculty of Arts and Sciences, Beijing Normal University, Zhuhai 519087, China 





4Faculty of Psychology, Beijing Normal University, Beijing 100875, China 





5Department of Physics, Faculty of Arts and Sciences, Beijing Normal University, Zhuhai 519087, China *zhuowang@bnu.edu.cn 



摘要：受人类皮肤的启发，仿生触觉传感以其灵活高效的感知能力，有效推动着诸多领域的发展与革新。光纤凭借其信息感知与传输能力及柔性特质，被视为触觉仿生领域极具前景的解决方案。本研究设计了一种基于柔性PDMS嵌入式光纤环形谐振器（FRR）的光纤触觉传感系统用于盲文识别，并采用Pound-Drever-Hall（PDH）解调方案以提升检测灵敏度。理论仿真与实验验证表明：通过仿生滑动探测方式结合多层感知器神经网络，单个具有硬度梯度设计的FRR可检测盲文字符中八种不同触觉压力，准确率达98.57%。进一步地，经训练测试后的MLP-LSTM模型对时序信号进行分类，实现了对盲文关键词与盲文诗歌的完全准确编码。本研究中光纤触觉传感系统的优势在于：高品质因子FRR可探测盲文点阵的细微差异；基于PDH频率解调的特性使其不受光功率波动影响；机器学习算法的应用能增强对轻微压力误差的鲁棒性并简化识别流程。该方案开创了一种全新的仿生触觉感知光学路径，在推动人机交互、智慧医疗等领域发展方面具有重要潜在价值。

$^ ©$ 2025 Optica Publishing Group 根据 Optica 开放获取出版协议的条款

# 1. 引言

人类触觉感知系统是一个由特殊细胞、神经和大脑区域组成的复杂网络，使我们能够感受和感知周围世界。它在日常活动中起着至关重要的作用，从拾取精细物体到在黑暗中导航环境[1]。触觉传感涵盖许多关键应用，包括智能机器人、仿生假肢、远程手术和人机界面（HMI）[2–4]。触觉压力传感器是智能机器人的关键组成部分。检测压力尤为重要，因为它使机器人能够感知、抓取和握持物体，提高这些传感器的灵敏度可增强其在这些任务中的性能[5,6]。此外，人类指尖的生物触觉感知涉及识别物体和表面纹理，这要求传感器结构具有高空间分辨率，并能对细微变化的动态压力做出快速响应[7,8]。在生命健康和辅助医疗领域，触觉感知同样发挥着

an important role. The emergence of bionic skin has effectively improved the quality of life of patients with burns and scalds. 

In addition to the above situations, the importance of tactile sense to the blind cannot be ignored. According to the World Health Organization’s (WHO) most recent data, at least 2.2 billion people globally have vision impairment. These individuals face challenges on daily activities and social interactions due to impaired visual function, which has become a significant public and social concern in contemporary society. Invented by Louis Braille in 1824, braille is an effective tool for blind and visually impaired people to acquire information by touching printed dots on a braille board with their fingers [9]. However, learning and reading braille can be challenging, prompting researchers to develop effective technology to assist blind individuals. 

There are two main approaches to braille recognition. One common approach is to acquire and preprocess braille images, and then extract information by analyzing the image features with computer algorithms. However, due to device limitations and the small size of braille characters, the vision-based scheme using image processing faces several challenges, including susceptibility to variations in ambient light and images taken from different distances and angles [10,11]. As an alternative scheme to acquire information about braille, the tactile sensing technique exhibits excellent performance while avoiding the aforementioned constraints and is expected to be an effective way to realize braille recognition. Electric tactile sensors are typically based on piezoresistance [12], piezoelectric [13], capacitive [10], and laser-induced graphene (LIG) [14] enabling the detection of subtle changes on touch surfaces. When a user touches the sensor surface with their finger, the sensor can detect the position and pressure of the contact point, subsequently converting this information into electrical signals. These signals, after processing, can be used to identify the braille characters being touched. Optical tactile sensors also hold significant potential in braille recognition, as these sensors detect changes in light to perceive touch position, pressure, and shape, thereby enabling the recognition of braille characters. Their operating principles often involve the reflection, refraction, or scattering of light. The main types of optical tactile sensors include micro-nano optical fiber sensors [15] and FBG sensors [16]. When combined with machine learning or pattern recognition techniques, these sensors can achieve automated braille recognition, converting physical tactile inputs into speech or text outputs, thus aiding visually impaired individuals in reading and accessing information more conveniently. Optical tactile sensors exhibit clear advantages in terms of precision, interference resistance, flexibility, and integration potential, particularly in complex environments or applications that demand high precision in braille recognition [17–19]. However, factors such as tactile detection sensitivity and environmental disturbances have always restricted the development of optical tactile sensors, making them less suitable for the recognition of smaller braille dots. 

In view of the advantages of optical sensors in tactile perception, this study proposes a method for braille recognition that combines high-precision fiber optic sensing methods with AI algorithms. The FRR has the advantages of simple preparation, flexible design, and high-quality factor, which is consistent with the material and sensitivity requirements needed as a bionic material. Here, one optical fiber tactile sensing system is reported, which utilizes a FRR as the sensor and employs the Pound-Drever-Hall (PDH) scheme for demodulation [20–23]. The FRR is encapsulated with PDMS to form an optical skin, and protrusions of different hardness are fixed on it to achieve effective recognition of different braille dot tactile pressure. The PDH interrogation signal is then used for braille recognition with the help of the MLP-LSTM machine learning algorithm. The advantage of combining PDH technology with machine learning algorithms to achieve braille recognition is that the high-quality factor resonator can distinguish the tiny pressure signals of braille dots, effectively improving the signal detection resolution, and the machine learning algorithm further improves the robustness and dynamics of the system, avoiding pressure errors caused by environmental factors. It not only realizes the efficient recognition and 

重要作用。仿生皮肤的出现有效改善了烧伤和烫伤患者的生活质量。

除了上述情况外，触觉对盲人的重要性也不容忽视。根据世界卫生组织（WHO）的最新数据，全球至少有22亿人存在视力障碍。这些人群因视觉功能受损而在日常活动和社会交往中面临挑战，这已成为当代社会一个重要的公共和社会关切点。由路易·布莱叶于1824年发明的盲文，是一种通过手指触摸盲文板上凸起的点来获取信息的有效工具，适用于盲人和视力受损者[9]。然而，学习和阅读盲文可能具有挑战性，这促使研究人员开发有效的技术来帮助盲人。

盲文识别主要有两种方法。一种常见方法是获取并预处理盲文图像，然后通过计算机算法分析图像特征来提取信息。然而，由于设备限制和盲文字符尺寸较小，基于视觉的图像处理方案面临诸多挑战，包括易受环境光线变化以及不同距离和角度拍摄图像的影响[10,11]。作为获取盲文信息的替代方案，触觉传感技术在避免上述限制的同时表现出优异性能，有望成为实现盲文识别的有效途径。电触觉传感器通常基于压阻[12]、压电[13]、电容[10]和激光诱导石墨烯（LIG）[14]等原理，能够检测触摸表面的细微变化。当用户用手指接触传感器表面时，传感器可检测接触点的位置和压力，随后将这些信息转换为电信号。这些信号经过处理后可用于识别被触摸的盲文字符。光学触觉传感器在盲文识别中也具有重要潜力，这类传感器通过检测光线变化来感知触摸位置、压力及形状，从而实现盲文字符识别。其工作原理常涉及光的反射、折射或散射。光学触觉传感器的主要类型包括微纳光纤传感器[15]和FBG传感器[16]。结合机器学习或模式识别技术，这些传感器可实现自动化盲文识别，将物理触觉输入转换为语音或文本输出，从而帮助视障人士更便捷地阅读和获取信息。光学触觉传感器在精度、抗干扰性、灵活性和集成潜力方面具有明显优势，尤其在复杂环境或对盲文识别精度要求较高的应用中表现突出[17–19]。然而，触觉检测灵敏度和环境干扰等因素始终制约着光学触觉传感器的发展，使其对更小盲文点的识别适应性不足。

鉴于光学传感器在触觉感知方面的优势，本研究提出了一种将高精度光纤传感方法与人工智能算法相结合的盲文识别方法。法布里-珀罗谐振腔（FRR）具有制备简单、设计灵活、品质因数高等优点，符合仿生材料所需的材质与灵敏度要求。本文报道了一种光纤触觉传感系统，该系统以FRR作为传感器，并采用Pound-Drever-Hall（PDH）方案进行解调[20–23]。通过将FRR封装在聚二甲基硅氧烷（PDMS）中形成光学皮肤，并在其表面固定不同硬度的凸起结构，实现了对不同盲文点触压力的有效识别。随后，借助MLP-LSTM机器学习算法，利用PDH解调信号进行盲文识别。将PDH技术与机器学习算法结合实现盲文识别的优势在于：高品质因数谐振腔能够区分盲文点的微小压力信号，有效提升信号检测分辨率；而机器学习算法进一步增强了系统的鲁棒性与动态性能，避免了环境因素导致的压力误判。该方法不仅实现了高效识别与

intelligent transcoding of braille information, but also has significant potential application value in fields such as human-computer interaction and intelligent manufacturing. 

# 2. Bionic optical fiber tactile sensing system

The biological tactile sensing system is an important condition for the survival of organisms. As shown in Fig. 1(a), human skin contains a variety of tactile sensors, which are then transmitted to the brain through the nervous system for information recognition and processing. Inspired by this principle, this study proposed a bionic tactile sensing system as shown in Fig. 1(b). An optical tactile bionic system for braille recognition is constructed, encompassing sensor structure design, optical fiber signal transmission, and AI algorithm-based information processing. The configuration of the optical fiber tactile sensing system for braille recognition is structured as follows in Fig. 2: A single-frequency tunable laser (NKT Photonics Koheras Basik E15) with a narrow linewidth $( < 0 . 1 \mathrm { k H z } )$ ) serves as the light source for the sensory system. The laser is driven by a triangular wave to sweep within a narrow range, producing a series of resonant peaks directly detected through the intensity of the transmitted light. The laser phase is modulated by a phase modulator (PM, iXblue photonics $\mathrm { L i N b } { \mathrm { O } } _ { 3 }$ ) driven by a sine wave signal M sin $2 \pi f _ { m } t$ , resulting 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/c06e4e115d09fb9940ead32ee9ae24f441d1010ceadb4746dd6ca2f2c84ae0db.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/404798c5f7598db37107d654105c7604da3b0254b225df6e3fae0cc764f5a240.jpg)



Fig. 1. (a)Schematic illustration of the biological tactile sensory system. (b) Schematic illustration of the bionic tactile sensory system. PM, electro-optic phase modulator; PD, photo-detector; ADC, analog-digital converter; DAC, digital-analog converter; SG, signal generator; LIA, lock-in amplifier; PI, proportional integral controller. (i) Schematic diagram of fiber optic resonator tactile sensor. The FRR is encapsulated with PDMS and rigid package, leaving only the sensing area (blue) exposed for braille recognition. (ii) Experimental diagram of optical fiber resonator tactile sensor. The encapsulated flexible sensor is fixed on the translation stage for braille recognition.


盲文信息的智能转码，而且在人机交互、智能制造等领域也具有显著的应用潜力。

# 2. 仿生光纤触觉传感系统

生物触觉传感系统是生物体生存的重要条件。如图1(a)所示，人类皮肤包含多种触觉传感器，这些信号随后通过神经系统传输至大脑进行信息识别与处理。受此原理启发，本研究提出了一种仿生触觉传感系统，如图1(b)所示。构建了一套用于盲文识别的光学触觉仿生系统，涵盖传感器结构设计、光纤信号传输以及基于AI算法的信息处理。用于盲文识别的光纤触觉传感系统配置如图2所示：采用窄线宽（ ${ < } 0 . 1 \ \mathrm { k H z } { \cdot }$ ）的单频可调谐激光器（NKT Photonics Koheras Basik E15）作为传感系统的光源。激光器由三角波驱动，在窄范围内扫描，产生一系列通过透射光强度直接检测的谐振峰。激光相位由正弦波信号M sin $2 \pi f _ { m } i$ t驱动的相位调制器（PM，iXblue photonics $\mathrm { L i N b O } _ { 3 } .$ ）进行调制，从而


(a) Biological tactile sensory system


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/6f9d8f5b58a0d6b6806d0b0f598cebe4539542961d30c11d697c4cb8c9649ac3.jpg)



(b) Bionic tactile sensory system


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/851dc20fd663e2adae621234662a5011e1ab9adda5bd28c829347e4073c8db9b.jpg)



图1. (a)生物触觉感知系统示意图。(b)仿生触觉感知系统示意图。PM，电光相位调制器；PD，光电探测器；ADC，模数转换器；DAC，数模转换器；SG，信号发生器；LIA，锁相放大器；PI，比例积分控制器。(i)光纤谐振腔触觉传感器示意图。FRR采用PDMS与刚性封装，仅留传感区域（蓝色）暴露用于盲文识别。(ii)光纤谐振腔触觉传感器实验示意图。封装后的柔性传感器固定在平移台上进行盲文识别。


in the generation of carrier and high-order sideband components. The error signal (also called the PDH curve) is demodulated using a lock-in amplifier (LIA), with the detailed theoretical derivation provided in Appendix A. The PDH error signal is then split into two branches for frequency synchronization and analysis. One branch is sent to a proportional-integral (PI) servo controller, where the PI controller is activated, and the laser sweep is disabled. The error signal is fed to the piezoelectric transducer (PZT) to modulate the laser frequency, enabling the closed-loop system to synchronize the laser frequency with the cavity resonance frequency. The other branch is extracted for further analysis and serves as the system output. 

When the FRR equipped with different gradient tactile pressure relief designs slides over the braille board, the pressure exerted by the raised braille dots causes slight changes in the length and refractive index of the optical fiber. These changes alter the phase of the light transmitted through the fiber, leading to a shift in the resonant frequency of the FRR. This frequency shift can be detected by the PDH system. As three raised dots can form eight different arrangements, the PDH system generates error signals corresponding to the pressure signals from these eight different arrangements. In practice, even for the same arrangement, there may be slight pressure differences when the FRR slides over the dots, resulting in signals that are not exactly identical. To address this, machine learning methods are employed to classify these signals using a large amount of experimental data. Through this processing and analysis, the corresponding arrangement of braille dots from the signals output by the PDH system is identified, thereby decoding the information conveyed by the braille. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/ac56e77c3b7815f62dedcc534cd0626f09f42b85021ff8e0623fa187eeee649e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/e26f4b9cae8d3a9f7aec4dcf2e1e8fc56b9eee1b2492cbc7944f71b800478027.jpg)



Fig. 2. Schematic configuration of the PDH system (a) and experimental setup (b). PM, electro-optic phase modulator; PD, photo-detector; LPF, low-pass filter; PI, proportional integral controller.


# 3. Theoretical analysis

# 3.1. Theoretical analysis of optical fiber tactile pressure sensing

External pressure applied to the FRR leads to resonance shifts due to the stress-strain and photo-elastic effects of the optical fiber. The stress-strain effect changes the length of the optical fiber, affecting the phase of the light wave traveling through it. Similarly, the photo-elastic effect impacts the refractive index of the optical fiber, also affecting the phase of the light wave. Under the influence of these combined effects, resonance shifts of the FRR ultimately occur. 

The phase of light transmitted in an optical fiber changes when the fiber is subjected to stress and temperature from external sources. When pressure is applied to an optical fiber, elastic deformation, caused by the stress-strain effect, occurs, leading to a change in the fiber’s length. Additionally, the photo-elastic effect alters the refractive index of the fiber core. Similarly, temperature variations modify the effective refractive index and length of the fiber, causing phase 

在载波和高阶边带分量的生成过程中。误差信号（也称为PDH曲线）通过锁相放大器（LIA）进行解调，详细的理论推导见附录A。随后，PDH误差信号被分成两个分支，分别用于频率同步和分析。一个分支被送入比例积分（PI）伺服控制器，此时PI控制器被激活，激光扫描功能被禁用。误差信号被馈送到压电换能器（PZT）以调制激光频率，使闭环系统能够将激光频率与腔共振频率同步。另一个分支则被提取用于进一步分析，并作为系统输出。

当配备不同梯度触觉压力缓解设计的FRR在盲文板上滑动时，凸起的盲文点施加的压力会导致光纤的长度和折射率发生微小变化。这些变化会改变通过光纤传输的光的相位，从而导致FRR的谐振频率发生偏移。这种频率偏移可以被PDH系统检测到。由于三个凸起点可以形成八种不同的排列方式，PDH系统会生成与这八种不同排列的压力信号相对应的误差信号。实际上，即使是同一种排列，当FRR滑过凸点时也可能存在轻微的压力差异，导致信号并非完全一致。为了解决这个问题，我们采用机器学习方法，利用大量实验数据对这些信号进行分类。通过这种处理和分析，可以从PDH系统输出的信号中识别出对应的盲文点排列，从而解码盲文所传递的信息。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/b40aaa4888bf81da49f80fb52fcda73f2afbed0c75fda04bd360593d54a4e7f2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/50fc29875269bcc65a2d584b277bdb39b7cc482263d0794286d46ef9a85810c9.jpg)



图2. PDH系统的原理配置图(a)和实验装置图(b)。PM，电光相位调制器；PD，光电探测器；LPF，低通滤波器；PI，比例积分控制器。


# 3. 理论分析

# 3.1. Theoretical analysis of optical fiber tactile pressure sensing

施加于光纤环形谐振器（FRR）的外部压力会因光纤的应力-应变效应和光弹效应导致谐振偏移。应力-应变效应会改变光纤的长度，从而影响在其中传播的光波的相位；类似地，光弹效应会改变光纤的折射率，同样影响光波的相位。在这两种效应的共同作用下，最终引发FRR的谐振偏移。

光在光纤中传输的相位会因外部应力与温度的影响而发生变化。当对光纤施加压力时，应力-应变效应会导致光纤发生弹性形变，从而改变其长度。此外，光弹性效应会改变纤芯的折射率。同样，温度变化也会改变光纤的有效折射率和长度，进而引起相位变化。

changes. These changes result in a phase shift in the light wave propagating through the fiber [24]. The optical fiber has a thermo-optic coefficient of $1 \times 1 0 ^ { - 5 \circ } C ^ { - 1 }$ and a coefficient of thermal expansion of $5 . 5 \times 1 0 ^ { - 6 \circ } C ^ { - 1 }$ . The braille recognition experiment is typically conducted at room temperature, where temperature variations have a negligible effect on the resonant frequency of the cavity compared to pressure-induced effects. The relationship between phase change and pressure and temperature variations can be expressed as: 

$$
\begin{array}{l} \Delta \phi = \Delta \phi_ {\sigma} + \Delta \phi_ {T} \\ = a _ {\sigma} \Delta P + a _ {T} \Delta T \tag {1} \\ \approx a _ {\sigma} \Delta P \\ \end{array}
$$

where $\Delta \phi _ { \sigma }$ and $\Delta \phi _ { T }$ are the phase change of the light through the fiber caused by applied pressure and temperature, respectively. $\Delta P$ and $\Delta T$ are the change of applied pressure and temperature. $a _ { \sigma }$ and $a _ { T }$ are the coefficients related to applied pressure and temperature changes. According to σthe resonance condition (5), $\frac { n _ { e f f } L } { c }$ is related to the resonance frequency. So the resonance shift of the optical resonator is proportional to the phase change of the light wave propagating within the cavity [25], and this relationship can be expressed as: 

$$
\begin{array}{l} \Delta \phi = \frac {2 \pi n _ {\text {e f f}} L}{c} \Delta f \\ = \frac {2 \pi q}{f _ {\text {r e s}}} \Delta f \tag {2} \\ = \frac {1}{b} \Delta f \\ \end{array}
$$

where $n _ { e f f }$ is the effective refractive index of optical fiber, $L$ is the length of resonator, $c$ is the light speed, $f _ { r e s }$ is the resonance frequency, and $\Delta f$ is the resonance shift of the resonator. According to Eq. (9), the voltage shift of the PDH error signal is proportional to the resonance shift. Therefore, the relationship between the voltage shift and the applied pressure can be concluded as follows: 

$$
\begin{array}{l} \Delta P = \frac {1}{k _ {0} b a _ {\sigma}} \Delta V \tag {3} \\ = K \Delta V \\ \end{array}
$$

where $b$ is a constant denoting the sensitivity of the system. 

# 3.2. Braille sensor parameters analysis and simulation

Before experimentation, performing simulations and analytical calculations is crucial to identify optimal experimental conditions. Figure 3(a) illustrates the overall sensing principle of the system. The resonant frequency of the FRR shifts in response to applied pressure, and this frequency shift is demodulated by the PDH system. The demodulated signal is then used as the system’s output to measure the pressure. The quality factor (Q) is a critical parameter for the FRR, characterizing its ability to couple and confine intracavity photon energy. The Q value of the resonant cavity can be influenced by various factors, such as the coupling coefficient, transmission loss, light source coherence, and external disturbances. In this study, the coupling coefficient and transmission loss are considered, as the two factors have significant effects on the Q value and can be controlled in the experiment. The value of Q can be calculated by $Q = f _ { 0 } / F W H M$ , where $f _ { 0 }$ represents the resonance frequency. In the simulation, the FRR was configured with the following parameters: an effective refractive index of the optical fiber of 1.45, a fiber length (L) of 2 meters, an initial laser wavelength of $1 5 5 0 \mathrm { n m }$ , and a laser linewidth of $1 0 0 \mathrm { H z }$ . Figure 3(b) presents the simulation results. This Q value directly indicates the detection sensitivity of the resonator. A high-Q 

变化。这些变化导致通过光纤传播的光波产生相移[24]。该光纤的热光系数为 $1 \times 1 0$ $^ { - 5 \mathrm { ~ o ~ } } C ^ { - 1 }$ ，热膨胀系数为 $5 . 5 \times 1 0 ^ { - 6 \circ } C ^ { - 1 }$ 。盲文识别实验通常在室温下进行，与压力引起的影响相比，温度变化对腔体谐振频率的影响可忽略不计。相位变化与压力及温度变化之间的关系可表示为：

$$
\begin{array}{l} \Delta \phi = \Delta \phi_ {\sigma} + \Delta \phi_ {T} \\ = a _ {\sigma} \Delta P + a _ {T} \Delta T \tag {1} \\ \approx a _ {\sigma} \Delta P \\ \end{array}
$$

其中 $\Delta \phi _ { \sigma }$ 和 $\Delta \phi _ { T }$ 分别表示由外加压力和温度引起的光纤中光波的相位变化， $\Delta P$ 和 $\Delta T$ 为外ϕσ ϕ加压力和温度的变化量， $a _ { \sigma }$ 和 $a _ { T }$ 是与外加压力和温度变化相关的系数。根据共振条件(5)， σneff L与共振频率相关。因此光学谐振器的共振偏移与腔内传播光波的相位变化成正比c[25]， 该关系可表示为：

$$
\begin{array}{l} \Delta \phi = \frac {2 \pi n _ {\text {e f f}} L}{c} \Delta f \\ = \frac {2 \pi q}{f _ {\text {r e s}}} \Delta f \tag {2} \\ = \frac {1}{b} \Delta f \\ \end{array}
$$

其中 $n _ { e f f }$ 是光纤的有效折射率，L是谐振腔的长度， $c$ 是光速， $f _ { r e s }$ 是谐振频率， $\Delta f$ 是谐振腔的谐振偏移。根据方程(9)，PDH误差信号的电压偏移与谐振偏移成正比。因此，电压偏移与施加压力之间的关系可归纳如下：

$$
\begin{array}{l} \Delta P = \frac {1}{k _ {0} b a _ {\sigma}} \Delta V \tag {3} \\ = K \Delta V \\ \end{array}
$$

其中b是一个常数，表示系统的灵敏度。

# 3.2. Braille sensor parameters analysis and simulation

在实验前，进行仿真和分析计算对于确定最佳实验条件至关重要。图3(a)展示了系统的整体传感原理。FRR的谐振频率会随施加的压力而偏移，该频移由PDH系统解调。解调后的信号随后作为系统输出用于压力测量。品质因数(Q)是FRR的关键参数，表征其耦合与限制腔内光子能量的能力。谐振腔的Q值受多种因素影响，例如耦合系数、传输损耗、光源相干性及外部干扰等。本研究主要考虑耦合系数与传输损耗，因为这两个因素对Q值影响显著且可在实验中调控。Q值可通过 $Q = f _ { 0 } / F W H M$ 计算，其中f0代表谐振频率。仿真中FRR配置参数如下：光纤有效折射率1.45、光纤长度(L)2米、初始激光波长1$5 5 0 \mathrm { n m }$ 、激光线宽 $1 0 0 \mathrm { H z } _ { \circ }$ 。图3(b)展示了仿真结果。该Q值直接反映了谐振器的检测灵敏度。高Q值

resonator is characterized by a narrower linewidth and exhibits a steeper slope of frequency discrimination sensitivity in the demodulation curve, allowing for the detection of larger signals even in response to minor resonant frequency shifts. According to the simulation results, the FRR was then constructed by connecting one input port and one output port of a commercial single-mode fiber $2 \times 2$ optic coupler. The coupling coefficient of the coupler was set to 0.1, and the length of the resonator fiber was 2 meters. The insertion loss of the coupler, measured using an optical power meter, was approximately 0.3 dB, while the connection loss was estimated to be around 0.2 dB. 

According to Eq. (8), the PDH curve after demodulation by the LIA amplifier is linear near the resonance of the FRR and crosses the zero point when the laser output frequency is exactly at the resonant frequency of the FRR. The slope of the linear region dictates the frequency discrimination sensitivity of the resonator, and its linear response range is approximately equal to the Full Width at Half Maximum (FWHM). The PDH error signal exhibits dependence on various parameters, including the structural parameters of the resonator, modulation depth, and modulation frequency. Figure 3(c) shows the simulation of the change in the zero-point slope under varying modulation voltages and modulation frequencies. Furthermore, formulas (8) and (9) show that once the structural parameters of the resonator are fixed, the frequency discrimination slope is only related to the modulation frequency, modulation depth, and phase difference between the error signal and the reference signal. According to the theory of coherent detection, the phase difference is adjusted through the phase shifter, and when the phase difference is π , $\frac { \pi } { 2 }$ the lock-in amplifier obtains the maximum error signal. Therefore, the frequency discrimination slope mainly depends on the modulation frequency and depth. 


(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/cff8e2c6030bbc40948e623453f6d46f69fd72b4520c88bd992c92cf88ddbf95.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/b48ff30911a5c46c5034464b51faefc6ade950825d516f01c3aaa715465ef807.jpg)



（c）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/39ded6ecd7fe2822973031bae2f9a1bfb5928faea71194de828edb111bd574f4.jpg)



Fig. 3. Principle of demodulation using PDH. (b) Simulation results of Q influenced by coupling coefficient and transmission loss. (c) Simulation results of zero-point slope influenced by modulation frequency and modulation voltage.


谐振器的特点是具有更窄的线宽，并在解调曲线中展现出更陡峭的频率鉴别灵敏度斜率，即使响应微小的谐振频率偏移也能检测到较大的信号。根据仿真结果，随后通过连接商用单模光纤 $2 { \times } 2$ 光学耦合器的一个输入端口和一个输出端口构建了FRR。耦合器的耦合系数设定为0.1，谐振器光纤长度为2米。使用光功率计测得耦合器的插入损耗约为0.3dB，而连接损耗估计约为 $0 . 2 \mathrm { d B }$ 。

根据公式(8)，经锁相放大器解调后的PDH曲线在FRR谐振点附近呈线性，且当激光输出频率恰好等于FRR谐振频率时通过零点。线性区域的斜率决定了谐振腔的频率鉴别灵敏度，其线性响应范围约等于半高全宽(FWHM)。PDH误差信号受多种参数影响，包括谐振腔结构参数、调制深度和调制频率。图3(c)展示了不同调制电压与调制频率下零点斜率的仿真变化。此外，公式(8)和(9)表明，一旦谐振腔结构参数确定，频率鉴别斜率仅与调制频率、调制深度以及误差信号与参考信号之间的相位差有关。根据相干检测理论，相位差通过移相器调节，当相位差为 2时，锁相放大器可获得最大误差信号。因此，频率鉴别斜率主要取决于调制频率与调制深度。


(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/6db2c1dd88e846a568349d63bd28f147c8307b7cf490d56b70971eb94b7eda34.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/914e8cecdcb5805114df81b7333227500328c9ba8772dbd6000b88498b775282.jpg)



（c）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/5346c728a3e04a318628cce5c8f56d1d6023a00705bc1087036e0eb7b3bee561.jpg)



图3. 采用PDH技术的解调原理。(b) 耦合系数与传输损耗对Q值影响的仿真结果。(c) 调制频率与调制电压对零点斜率影响的仿真结果。


# 4. Experiment

# 4.1. Fabrication of braille sensor

To differentiate between various braille arrangements in a single column (three rows and one column), we propose a novel sensor structure.As shown in Fig. 4 Step 1, a 3D-printed mold designed by solidworks was used for fiber packaging. Firstly, the PDMS precursor and curing agent were mixed at a ratio of 10:1, and the mixture was left at room temperature for 20 minutes to remove bubbles. The optical fiber was placed into the mold, the PDMS solution was injected into it, and the assembly was cured on a heating plate at $8 0 ^ { \circ } \mathrm { C }$ for 20 minutes. Furthermore, PDMS was injected onto the packaged fiber surface to form three protrusions with different hardness levels, as the solutions were made by mixing different proportions. When the optical fiber slides over braille, the variations in the arrangement of braille dots cause distinct effects on the fiber due to material differences, with harder protrusions exerting more pronounced impacts. The positions of the protrusions in the sensing region align with the braille dots, with a spacing of approximately $2 . 5 \mathrm { m m }$ . After demolding from the 3D-printed mold, the region surrounding the three protrusions is carefully trimmed into an approximately rectangular shape. The exact dimensions of the rectangular are not strictly specified, as long as it fully encompasses the three protrusions and is kept as small as possible to facilitate the subsequent packaging of the FRR. The core component of the sensor is the FRR, which can be easily constructed by connecting one input port and one output port of commercial $2 { \times } 2$ fiber coupler, as shown in Fig. 4 Step 2. The structure and principle of the FRR are described in Appendix A. In our experiments, the FRR used had a coupling ratio of 9:1 and was sensitive to external disturbances. The sensing region was then connected into the resonator. To mitigate potential interferences effects, Only a small portion of the ring resonator is exposed as the sensing region, eliminating potential interferences unrelated to the sensor’s function. As shown in Fig. 4 Step 3, the ring resonator and coupler of the FRR are enclosed in a rigid protective shell to shield the resonator from interference caused by human or robotic interaction during braille recognition. Figure 4(b) presents photographs of the device captured during the sensor manufacturing process. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/eb6cb1e46209120fbe7e5534fabe3951bd9285259c390510331242c38d4a378d.jpg)



Fig. 4. (a) The schematic diagrams of the sensor fabrication process.(b) The corresponding images of the actual fabricated device of each step.


# 4. 实验

# 4.1. Fabrication of braille sensor

为了区分单列（三行一列）中的不同盲文排列，我们提出了一种新颖的传感器结构。如图4步骤1所示，采用SolidWorks设计并通过3D打印制作的模具用于光纤封装。首先，将PDMS预聚物与固化剂以10:1的比例混合，混合物在室温下静置20分钟以去除气泡。将光纤放入模具中，注入PDMS溶液，随后在 $8 0 ^ { \circ \circ } \mathrm { C }$ 的加热板上固化20分钟。此外，通过在混合时调整不同比例，将PDMS溶液注入已封装的光纤表面，形成三个不同硬度的凸起结构。当光纤滑过盲文时，盲文点排列的变化会因材料差异对光纤产生不同影响，其中较硬的凸起会产生更显著的作用。凸起在传感区域的位置与盲文点对应，间距约为2.5毫米。从3D打印模具脱模后，将三个凸起周围区域精细修剪为近似矩形。矩形尺寸无需严格限定，只需完全覆盖三个凸起并尽可能缩小面积，以便后续进行FRR封装。传感器的核心部件是FRR（光纤环形谐振器），如图4步骤2所示，可通过连接商用 $2 \times 2$ 光纤耦合器的一个输入端口和一个输出端口轻松构建。FRR的结构与原理详见附录A。实验中使用的FRR耦合比为9:1，对外界扰动敏感。随后将传感区域接入谐振器。为减少潜在干扰，仅将环形谐振器的一小部分作为传感区域暴露，从而消除与传感器功能无关的干扰。如图4步骤3所示，FRR的环形谐振器与耦合器被封装在刚性保护壳内，以防止盲文识别过程中人或机器人操作带来的干扰。图4(b)展示了传感器制造过程中拍摄的器件实物照片。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/2a54f780ff8efab6896dcd640ca0ea2c91a932e033ee26d19131c15f28e64b51.jpg)



图4. (a) 传感器制造工艺的示意图。(b) 各步骤实际制造器件的对应图像。


# 4.2. Characteristics analysis of braille sensor

The transmission spectrum of the FRR was characterized by scanning the tunable laser source across its resonance peak. This was achieved by driving the laser’s piezoelectric transducer (PZT) with a triangular wave signal at a frequency of $1 0 \ : \mathrm { H z }$ and a peak-to-peak voltage of 1 Vpp. To generate the PDH error signal, a narrow-linewidth tunable laser source was phase-modulated with a sinusoidal driving signal at a frequency of $9 0 0 \mathrm { k H z }$ and a peak-to-peak voltage of 400 mVpp, which is lower slightly than the PD output power. The PD output signal was mixed with the reference signal that has the same frequency as the modulation signal. The phase of the reference signal is adjusted by a phase shifter to maximize the error signal. Then a fourth-order Butterworth low-pass filter was implemented to eliminate high-frequency components, enabling the acquisition of the PDH error signal. The PDH error signal is split into two branches. One branch of the PDH error signal is fed to a PI servo controller to form a closed loop, which generates a control signal for synchronizing the laser frequency to the cavity resonance frequency. The other branch is recorded by the oscilloscope as the sensor system output for further analysis. Figure 5(a,b) shows the transmission spectrum under modulation and its demodulation curve. Estimation through experimental data shows that the FRR has an extremely narrow full width at half maximum (FWHM) of $0 . 1 \mathrm { p m }$ . The PDH error signal exhibits an excellent linearity of 31.65 V/pm near the resonance and has a wide dynamic range of $5 5 \mathrm { m V } .$ 

A manual force tester equipped with a digital force gauge (Handpi instruments HP-500) is used to provide external pressure in the experiment for testing the characterization of force sensing to provide external pressure. The voltage of the PD output increased slightly corresponding to the applied pressure because of resonance shift, while the peak voltage did not reach the maximum and then recovered to the minimum value as the closed-loop system worked. Three cylindrical PDMS protrusions were secured on the FRR to measure the responses of the FRR to static pressure. To achieve a gradient of hardness, The PDMS solution was fabricated by adjusting the weight ratios of precursor and curing agent in various mass ratios of 5:1, 10:1, and 20:1 to achieve different hardness of the protrusions after curing. These protrusions were then secured on the optical skin. 

The experiment measured the pressure response of the sensor at three points within the range of $_ { 0 - 3 } \mathrm { N }$ , which aligns with the typical pressure exerted by a human finger when touching a braille character. Meanwhile, the system’s output response remains within the optimal measurement range. Figure 5(c) shows the system’s voltage shift recorded under different forces using PDMS protrusions with three hardness levels (ratios of 5:1, 15:1, and 25:1). Acting as probes, the PDMS protrusions compress against the sample surface, transferring the applied pressure to the optical fiber. The resonance frequency shift becomes more pronounced under identical pressing strokes when the sample is harder. Typically, the detection limit of the sensor is approximately $1 0 0 ~ \mathrm { m N }$ at a PDMS ratio of 10:1. Furthermore, linear fitting was performed in Fig. 5(d) to analyze the relationship between the voltage shift and the applied pressure for the three different hardness protrusions. The figure indicates that the system feedback voltage increased more under the same press force when the protrusion was harder, as more deformation was taken by the resonator. The slopes of the fitting curves are $0 . 0 5 8 ~ \mathrm { N / m V } .$ , $0 . 0 7 1 ~ \mathrm { N / m V } ,$ , and 0.083 $\mathrm { N } / \mathrm { m V } ,$ respectively. Figure 5(e) shows the output voltage shift of the PDH error signal as the environmental temperature increases from $2 0 ^ { \circ } \mathrm { C }$ to $3 5 ^ { \circ } \mathrm { C }$ in $5 ^ { \circ } \mathrm { C }$ increments. The overall fluctuation error of the test data is less than $1 . 5 \mathrm { m V }$ , indicating a stable performance. As shown in Fig. 5(f), The PDH error signals exhibit an overall fluctuation error of less than $1 . 8 4 ~ \mathrm { m V }$ by alternatively changing the applied pressures from $1 \mathrm { \Delta N }$ to $3 \mathrm { ~ N ~ }$ for 20 circles. The standard deviations recorded were 0.67 mV, $0 . 4 8 \mathrm { m V }$ , and $0 . 5 7 \mathrm { m V }$ for applied pressures of 1 N, 2 N, and 3 N, respectively. The results show that the FRR sensor system exhibits excellent stability. 

Furthermore, the stability of the sensor was tested under changing temperature conditions. The air conditioner was set to cooling mode with the temperature set at $2 3 ^ { \circ } \mathrm { C }$ , and a thermometer 

# 4.2. Characteristics analysis of braille sensor

FRR的透射光谱通过扫描可调谐激光源跨越其共振峰来表征。这是通过使用频率为10 Hz、峰峰值电压为1 Vpp的三角波信号驱动激光器的压电换能器（PZT）实现的。为生成PDH误差信号，采用窄线宽可调谐激光源进行相位调制，调制信号为正弦驱动信号，频率为 $9 0 0 \mathrm { k H z }$ 、峰峰值电压为 $4 0 0 \mathrm { m V p p }$ ，略低于PD输出功率。PD输出信号与和调制信号同频的参考信号进行混频。通过移相器调节参考信号的相位，以最大化误差信号。随后采用四阶巴特沃斯低通滤波器消除高频分量，从而获取PDH误差信号。PDH误差信号被分为两路：一路馈入PI伺服控制器形成闭环，产生控制信号以实现激光频率与腔共振频率的同步；另一路由示波器记录，作为传感器系统输出供进一步分析。图5(a,b)展示了调制下的透射光谱及其解调曲线。通过实验数据估算，FRR的半高全宽（FWHM）极窄，仅为 $0 . 1 \mathrm { p m } _ { \mathrm { c } }$ 。PDH误差信号在共振点附近表现出优异的线性度（ $( 3 1 . 6 5 \mathrm { V / p m } )$ ），并具有 $5 5 \mathrm { m V }$ 的宽动态范围。

实验中采用配备数字测力计（Handpi仪器HP-500）的手动测力仪提供外部压力，以测试力传感特性。由于共振偏移，PD输出电压随施加压力略有上升，但峰值电压未达最大值，随后在闭环系统作用下恢复至最小值。三个圆柱形PDMS突起被固定在FRR上以测量其对静态压力的响应。为实现硬度梯度，通过调整预聚体与固化剂的质量比（分别为5:1、10:1和20:1）制备PDMS溶液，使固化后的突起获得不同硬度。这些突起随后被固定在光学皮肤表面。

实验在0–3 N范围内选取三个点测量了传感器的压力响应，该范围与人类手指触摸盲文字符时的典型压力相符。同时，系统的输出响应始终保持在最佳测量范围内。图5(c)展示了使用三种硬度（配比为5:1、15:1和25:1）的PDMS凸起在不同压力下记录的系统电压偏移。作为探针的PDMS凸起会压缩样品表面，将施加的压力传递至光纤。当样品硬度较高时，在相同按压行程下共振频率偏移更为显著。通常情况下，在PDMS配比为10:1时传感器的检测限约为 $1 0 0 \mathrm { m N } ,$ 。此外，图5(d)通过线性拟合分析了三种不同硬度凸起的电压偏移与施加压力之间的关系。图中表明，当凸起硬度更高时，在相同压力下系统反馈电压增幅更大，因为谐振器承担了更多形变。拟合曲线的斜率分别为 $0 . 0 5 8 \mathrm { N } / \mathrm { m V }$ 、 $0 . 0 7 1 \mathrm { N / m V }$ 和 $\mathrm { 0 . 0 8 3 N / m V }$ 。图5(e)展示了环境温度从 $2 0 ^ { \circ \circ } \mathrm { C }$ 升至 $3 5 ^ { \circ \circ } \mathrm { C }$ （以 $5 ^ { \circ } \mathrm { { ^ C } }$ 为增量）时PDH误差信号的输出电压偏移。测试数据的整体波动误差小于 $1 . 5 \mathrm { m V }$ ，表明性能稳定。如图5(f)所示，通过在1 N至3 N压力间交替切换进行20次循环测试，PDH误差信号的整体波动误差小于 $1 . 8 4 \mathrm { m V }$ 。在施加压力为1 N、2 N和3 N时记录的标准偏差分别为0.$6 7 \mathrm { m V }$ 、 $0 . 4 8 \mathrm { m V }$ 和 $0 . 5 7 \mathrm { m V } .$ 。结果表明该FRR传感器系统具有优异的稳定性。

此外，在温度变化条件下测试了传感器的稳定性。空调设置为制冷模式，温度设定为23◦C，并使用温度计

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/0470f0839e67277ee3cc4637988755525b8e95fe1a4ce62b21cf46d7e757c5b7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/2dbadac67d6609b5f60847ee34178da51b74e87702a185fc0c043872e658996e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/ff82733c6275d59a60f9e94b2d51832671b55aba54d073237e0b1b1c7c12be9c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/dd9c9c3b71b88aab0be408b0df5df771b936e7217fcb7b4757c0cd93f0178911.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/5d923ddf1a62f5c5a9f47f4b24d85cdf4bdfefb832fde6f07ad61e6e92e51dc9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/33e6e208ae7154339bb28410f814a028df00737ed846f764e467dca266914627.jpg)



Fig. 5. (a,b) Transmission spectrum and demodulation curve of the tactile sensor system output.(c) Relationship between PDH error signal voltage variation and applied pressure curve. (d) Curve fitting relationship between applied pressure and voltage variation within the range of 0-3N. (e) The output of the sensor under different applied pressures (1-3 N) when external temperature changes. (f) The repeatability of the sensor is tested by alternately switching the applied pressure among 1N, 2N, and 3N.


was used to record temperature data at one-minute intervals. Figure 6(a) shows the process of change during temperature decreasing and recovering. Two time periods, each lasting 2 minutes, were selected for stability testing. The first period featured rapid temperature changes of $0 . 3 ^ { \circ } \mathrm { C } / \mathrm { m i n }$ during the decreasing phase, and the second period had a rate of $0 . 1 ^ { \circ } \mathrm { C } / \mathrm { m i n }$ during the recovery phase. The sensor was slid over the braille with different dots arrangements. Each dots arrangement was tested 5 times in total,and the difference between the highest and lowest output voltages was calculated. As shown in Fig. 6(b), the maximum voltage difference was $1 . 8 \mathrm { m V }$ during the decreasing process, and $1 . 5 \mathrm { m V }$ during the recovering process. The voltage 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/8d003951bb61f0659a9dd1d83bbf8a4bd16238f6118b9ce49fbdfa2f985a31e7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/f69b04884e0d8c446150cca11637cc95bd1fdc5ab26a869707bdc2bcf4ed1239.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/0b4efd7d66d15ead79e2a922da8e8ff7e52aa4dbb599e8b3845a46b535162b0e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/1aac142c78728cb881f2d8518740af88cd950e825f8a6a2ca60bb67e85bda35f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/b1b0d3bc882996995317f98fc15ae3b5a2193d057769c2909407bd9c61fd9792.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/78edacd064c28392e6e989bacab2022dbe52c34c8a16b8ffc595760005b4aa99.jpg)



图5. (a,b) 触觉传感器系统输出的透射谱与解调曲线。(c) PDH误差信号电压变化量与施加压力的关系曲线。(d) 0-3N范围内施加压力与电压变化的曲线拟合关系。(e)外部温度变化时传感器在不同施加压力(1-3 N)下的输出。(f) 通过在1N、2N和3N之间交替切换施加压力来测试传感器的重复性。


用于以每分钟一次的间隔记录温度数据。图6(a)展示了温度下降和恢复期间的变化过程。选取了两个各持续2分钟的时间段进行稳定性测试。第一个时间段在温度下降阶段以0. $3 ^ { \circ \circ } \mathbf { C } /$ 分钟的速度快速变化，第二个时间段在恢复阶段的变化速率为 $0 . 1 ^ { \circ \circ } \mathrm { C } / $ 分钟。传感器在不同点字排列的盲文上滑动测试。每种点字排列共测试5次，并计算最高与最低输出电压的差值。如图6(b)所示，下降过程中的最大电压差为 $1 . 8 \mathrm { m V }$ ，恢复过程中的最大电压差为 $1 . 5 \mathrm { m V }$ 。电压

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/50138400e7f9dfd9644a6118dd21fc9b86d68d9c77aac8bb60da49f53e4ad399.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/ae7430d1a2538ec6b6fb86375c794c11100cbcd68964a38e048a2de81ca02d7e.jpg)



Fig. 6. (a) Temperature change curve. (b) Voltage differences for different braille arrangements as the sensor slides across the braille.


fluctuations remained within the controllable range and did not affect the experimental results. The results indicate that tiny fluctuation of room temperature will have a minor impact on the system output, but will not influence the recognition accuracy. 

# 4.3. Intelligent braille recognition assisted by AI

Characters in braille are represented by a cell constructed of six raised dots that are arranged in three rows and two columns. The blind touch the braille with their fingers to perceive the arrangement of the braille dots on it. This process relies on the sense of touch. After knowing the arrangement of the braille dots, the blind can translate it into understandable language by comparing the braille and language (such as English) they have learned. Based on this method, a 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/fbba85446ff9b1684e8c1d860902502d5932bfc298e2494a1f59a15538b378b7.jpg)



Fig. 7. The flowchart of the algorithm for braille recognition.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/aa1e5fd75e91edaf6a997defc8d5b2742420fc7602f32b07062123bc20dd2a46.jpg)



图6. (a) 温度变化曲线。(b) 传感器滑过盲文时，不同盲文排列对应的电压差。


波动保持在可控范围内，并未影响实验结果。结果表明，室温的微小波动会对系统输出产生轻微影响，但不会影响识别精度。

# 4.3. Intelligent braille recognition assisted by AI

盲文中的字符由一个由六个凸点构成的单元格表示，这些点排列成三行两列。盲人通过手指触摸盲文来感知其上盲文点的排列。这一过程依赖于触觉。在了解盲文点的排列后，盲人可以通过对比已学习的盲文和语言（如英语），将其转化为可理解的语言。基于这种方法，一种

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/369d534129fb0955f5f693d477200cbba106e54d8e5afefaefe44a30600ffbac.jpg)



图7. 盲文识别算法流程图。


biomimetic sliding strategy is further proposed to achieve real-time and effective recognition of braille characters with the assistance of artificial intelligence (AI). As the sensor slides across the braille surface, different dot arrangements produce different amplitudes of pressure, with the signal of each character composed of two tactile pressures. The braille information is embedded within the time-series signals formed by the tactile pressures. 

Figure 7 shows the process of intelligent braille recognition. The arrangement of three dots generates seven distinct pressure signals, along with a zero-pressure signal, so accurately distinguishing these different amplitudes of pressure signals is fundamental to recognizing braille information. When the sensor slides over the braille, the contact force is not always the same. Using a neural network, we can classify the output signals for different arrangements, allowing for small differences in contact force during the sliding process. To improve the recognition accuracy and system versatility, the braille bumps corresponding to arrangements and combinations of three points are tested with a Multilayer Perceptron (MLP) Neural Network [26,27]. The database is composed of tactile pressure signals produced by contact between the sensor and the braille board during the sliding process. It is divided into training and testing datasets according to a 4:1 ratio. Each signal is labeled with the corresponding dot arrangements and subsequently transformed into a tensor. These tensors are then input into a fully connected three-layer perceptron neural network, which is utilized to estimate the target dot arrangements. When the tactile pressure signal is input into the trained network, the dot arrangements can be read out. Furthermore, to achieve the classification and recognition of English words and sentences with contextually related features, a long short-term memory (LSTM) machine translation model was trained using 5 English words [28]. 

Figure 8(a) illustrates the tactile pressure signals associated with the recognition of braille representations of English characters. The signal comprises a sequence of tactile pressure inputs, facilitating the identification of individual braille characters. For each column of three dots, excluding the all-flat configuration, there are seven possible raised dot patterns. As the optical fiber slides over the braille, the varying dot positions create different pressure levels on the fiber. A neural network is used to distinguish the signals generated by these varying pressures. The confusion matrix in Fig. 8(b) left shows that the classification accuracy reaches 


(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/a412659422e55ed2f8a5d3e0381db603fa03ed51a355eae9726573c5734347ba.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/67ba577aaf977a13dd3b13c456eafd2ee51fa4b60cf3de5d3b7d1270d2212dbe.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/56da6e8690ffa663501a60bd3d594281642f1b7d02aa35448898b14e55c99321.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/3bd7c683098695178e1b511f8626498726688d46d31d2344485ec424817b2c11.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/d52f05ac8910efadefb168161eaea3984c5df910a38422e92fcc1ff1906a3530.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/af51e4988d595db88874fc6f28d3bc2800d461ef644ad782ed5726b1f0a7ab5c.jpg)



Fig. 8. (a) The signal feedback and display of recognition results of the braille characters on an oscilloscope. (b) Classification results of MLP and LSTM machine learning algorithms using confusion matrices. (c,d) braille recognition results in different braille sentences based on handheld and mechanical methods.


仿生滑动策略被进一步提出，在人工智能（AI）的辅助下实现盲文字符的实时有效识别。当传感器滑过盲文表面时，不同的点阵排列会产生不同幅度的压力，每个字符的信号由两个触觉压力组成。盲文信息嵌入在由触觉压力形成的时间序列信号中。

图7展示了智能盲文识别的过程。三个点的排列会产生七种不同的压力信号以及一个零压力信号，因此准确区分这些不同幅度的压力信号是识别盲文信息的基础。当传感器滑过盲文时，接触力并非始终一致。通过使用神经网络，我们可以对不同排列的输出信号进行分类，从而允许滑动过程中接触力存在微小差异。为提高识别准确性和系统通用性，采用多层感知器（MLP）神经网络对三个点排列组合对应的盲文凸点进行了测试[26,27]。数据库由滑动过程中传感器与盲文板接触产生的触觉压力信号构成，按4:1的比例划分为训练集和测试集。每个信号均标注对应的点排列方式，随后转换为张量。这些张量被输入到全连接的三层感知器神经网络中，用于估计目标点排列。当触觉压力信号输入训练好的网络时，即可读取点排列信息。此外，为实现具有上下文关联特征的英文单词及句子的分类识别，采用5个英文单词训练了长短期记忆（LSTM）机器翻译模型[28]。

图8(a)展示了与识别英文盲文字符相关的触觉压力信号。该信号由一系列触觉压力输入组成，有助于识别单个盲文字符。对于每列三个点（排除全平配置），存在七种可能的凸起点图案。当光纤滑过盲文时，不同点的位置会在光纤上产生不同的压力水平。神经网络被用于区分这些不同压力产生的信号。图8(b)左侧的混淆矩阵显示，分类准确率达到


(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/9d917cda483cb40f3ce1a8af524c27a329e2a4c8fb86bb1038619e4c4562c066.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/e385963308a56af844c0ef5f194b49822a816873f5e84eb6ad7000b85befa06b.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/b976a355871950ab7a7398c12936dd57f318db833c00a58eaa4a13828491ff27.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/9048b4b16c190485308359efe3736786c8c9cdc021ea80cb3b00864532deec75.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/875c35cef98ee4db5649f95f1e403ab6a19502ccd2607aee8e35ea796d5d92af.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/581163c95926c76a4f0fa153b1540f6bb21cf45216b9dfabe04ff06b5108a043.jpg)



图8. (a) 盲文字符识别结果的信号反馈与示波器显示。(b) 使用混淆矩阵展示MLP和LSTM机器学习算法的分类结果。(c,d) 基于手持式与机械式方法在不同盲文句子中的识别结果。



Table 1. Comparison of braille recognition using different sensors and machine learning algorithms


<table><tr><td>Ref.</td><td>Sensing mechanisms</td><td>Algorithm</td><td>Datasets</td><td>Accuracy</td></tr><tr><td>[11]</td><td>vision-based tactile sensor</td><td>YOLO v8</td><td>450 labelled real sharp images</td><td>87.5% at 315 wpm</td></tr><tr><td>[12]</td><td>piezoresistive sensor</td><td>Random Forests (RDFA)</td><td>26 English letters and common punctuation marks</td><td>99%</td></tr><tr><td>[14]</td><td>triboelectric nanogenerator-based tactile sensor</td><td>one-dimensional Convolution Neural Network (1D CNN)</td><td>11-digit phone numbers</td><td>96.12%</td></tr><tr><td>[29]</td><td>capacitive tactile sensor</td><td>Long Short-Term Memory (LSTM)</td><td>Braille letters from &quot;A&quot; to &quot;Z&quot; as well as &quot;space&quot;</td><td>97%</td></tr><tr><td>[13]</td><td>piezoelectric and piezoresistive dual-mode tactile sensor</td><td>CNN-LSTM neural network</td><td>20 kinds of braille</td><td>90.58% in double mode</td></tr><tr><td>[16]</td><td>FBG sensor</td><td>none</td><td>5 characters</td><td>none</td></tr><tr><td>[30]</td><td>FBG sensor</td><td>random forest and back propagation neural network</td><td>2 words</td><td>none</td></tr><tr><td>[15]</td><td>micro-nano optical fiber sensor</td><td>LSTM neural network</td><td>22 and 26 characters</td><td>98.58%(22 characters) and 97.10%(26 characters)</td></tr><tr><td>This work</td><td>optical fiber resonator sensor and PDH demodulation</td><td>MLP-LSTM model</td><td>7 dots arrangements and 5 English letters as well as poetry sentences</td><td>98.57% (dots) and 100%(letters and sentences)</td></tr></table>

$9 8 . 5 7 \%$ . Furthermore, to better demonstrate the system’s ability to process and interpret braille information, 5 English words were selected, and an LSTM neural network was applied to classify the time-series signals generated by these 5 words. Figure 8(b) right shows a classification accuracy of $1 0 0 \%$ , which means that even if there are slight errors in the recognition of each column, they do not affect the overall understanding of braille. As illustrated in the Fig. 8(b), even when the sensor introduces minor errors in classifying the pressure signals, the LSTM model effectively mitigates the impact of these errors during the translation of the digital sequence into English text. Based on the MLP-LSTM model, we hope to get an English sentence. It is significant to keep the contact force consistency between sensor and braille for the accuracy of the signal of the sensor. So, the sensor was fixed on an electric displacement stage to recognize braille sentences. Figure 8(c) shows the original signal of braille recognition, the transcoded sentence, and the actual pictures of the experimental process. The figure shows the displacement stage and the process of human using the packaged sensor to conduct actual experiments. Furthermore, to expand the application scenarios of the sensor, we conducted braille recognition experiments by carefully holding and sliding the sensor manually. Similarly, Fig. 8(d) show the process of recognition through handheld sensor. 

Table 1 compares the accuracy of braille recognition using different sensors and machinelearning algorithms proposed by the authors. The basic principles of fiber optic sensors and electrical braille sensors, the auxiliary algorithms involved, and the final braille recognition accuracy are listed in the table. It can be seen that the FRR demodulated by the PDH technology 


表1. 使用不同传感器和机器学习算法进行盲文识别的比较


<table><tr><td>Ref.</td><td>Sensing mechanisms</td><td>Algorithm</td><td>Datasets</td><td>Accuracy</td></tr><tr><td>[11]</td><td>vision-based tactile sensor</td><td>YOLO v8</td><td>450 labelled real sharp images</td><td>87.5% at 315 wpm</td></tr><tr><td>[12]</td><td>piezoresistive sensor</td><td>Random Forests (RDFA)</td><td>26 English letters and common punctuation marks</td><td>99%</td></tr><tr><td>[14]</td><td>triboelectric nanogenerator-based tactile sensor</td><td>one-dimensional Convolution Neural Network (1D CNN)</td><td>11-digit phone numbers</td><td>96.12%</td></tr><tr><td>[29]</td><td>capacitive tactile sensor</td><td>Long Short-Term Memory (LSTM)</td><td>Braille letters from &quot;A&quot; to &quot;Z&quot; as well as &quot;space&quot;</td><td>97%</td></tr><tr><td>[13]</td><td>piezoelectric and piezoresistive dual-mode tactile sensor</td><td>CNN-LSTM neural network</td><td>20 kinds of braille</td><td>90.58% in double mode</td></tr><tr><td>[16]</td><td>FBG sensor</td><td>none</td><td>5 characters</td><td>none</td></tr><tr><td>[30]</td><td>FBG sensor</td><td>random forest and back propagation neural network</td><td>2 words</td><td>none</td></tr><tr><td>[15]</td><td>micro-nano optical fiber sensor</td><td>LSTM neural network</td><td>22 and 26 characters</td><td>98.58%(22 characters) and 97.10%(26 characters)</td></tr><tr><td>This work</td><td>optical fiber resonator sensor and PDH demodulation</td><td>MLP-LSTM model</td><td>7 dots arrangements and 5 English letters as well as poetry sentences</td><td>98.57% (dots) and 100%(letters and sentences)</td></tr></table>

$9 8 . 5 7 \%$ 。此外，为更好地展示系统处理与解读盲文信息的能力，我们选取了5个英文单词，并应用LSTM神经网络对由这5个单词产生的时序信号进行分类。图8(b)右侧显示分类准确率达到 $1 0 0 \%$ ，这意味着即使每列识别存在微小误差，也不会影响对盲文的整体理解。如图8(b)所示，即使传感器在压力信号分类中引入轻微误差，LSTM模型在将数字序列翻译为英文文本时也能有效减轻这些误差的影响。基于MLP-LSTM模型，我们希望获得完整的英文句子。保持传感器与盲文间的接触力一致性对传感器信号的准确性至关重要，因此我们将传感器固定在电动位移台上以识别盲文句子。图8(c)展示了盲文识别的原始信号、转码后的句子以及实验过程的实际照片。图中呈现了位移台及操作人员使用封装传感器进行实际实验的过程。此外，为拓展传感器的应用场景，我们通过人工精细持握并滑动传感器进行了盲文识别实验。类似地，图8(d)展示了通过手持传感器进行识别的过程。

表1比较了作者提出的使用不同传感器和机器学习算法进行盲文识别的准确性。表中列出了光纤传感器和电盲文传感器的基本原理、涉及的辅助算法以及最终的盲文识别准确率。可以看出，通过PDH技术解调的FRR

proposed in this study combined with machine learning has unique advantages in achieving accurate and fast braille recognition. The recognition accuracy is better than other sensor and algorithm combinations. By training the network with a wider range of words and sentences, full translation capabilities can be achieved without the need for individuals to laboriously learn braille rules. 

# 5. Conclusion

In this study, the optical fiber tactile sensing system using a flexible FRR for braille recognition is proposed, in which the FRR is packaged using a PDMS solution with a 3D-printed mold to form a flexible optical skin. The PDH optical frequency locking technique is used to interrogate tactile pressure and convert frequency fluctuations into voltage shifts. The performance of the pressure response is illustrated by experiments: through theoretical analysis and optimization of the sensor and closed-loop system parameters, high precision, and fast measurements are enabled. The PDH demodulation curve exhibits a steep linear slope, enabling high sensitivity and high resolution of the sensing system. The system’s linear region of the PDH error signal extends up to approximately $5 5 \mathrm { m V }$ , which is responsive to tactile pressure ranging from 0 to 3 N. By adjusting the closed-loop PDH system parameters, the average response time to tactile pressure is reduced to less than 0.1s, meeting the requirements for fast dynamic response in braille reading. Furthermore, the sensing system is utilized for continuous braille character recognition by implementing a biomimetic sliding approach with the assistance of artificial intelligence. To achieve effective decoding of braille dot patterns through tactile pressure feedback, three small protrusions with different hardness are secured on the resonator to transfer different exerted pressures. Eight different arrangements composed of three dots are fully distinguished using a Multilayer Perceptron Neural Network, achieving a classification accuracy of $9 8 . 5 7 \%$ . Consequently, all braille information, including letters, numbers, and punctuation, can be interpreted as the sensor slides over the braille board. The LSTM neural network is applied to classify the time-series signals generated by 5 words, and the classification accuracy of $1 0 0 \%$ means that even if there are slight errors in the recognition of each column, it will not affect the transcoding of the braille. The fiber optic tactile sensing system uses the high-quality factor FRR and PDH demodulation method to achieve tactile pressure resolution of general braille dots, effectively distinguishing eight different braille arrangements. Then, with the assistance of machine learning algorithms, it achieves accurate transcoding of braille information, effectively overcoming the influence of error factors. The research of Bionic tactile sensor based on flexible optical FRR will further promote the advancement of tactile sensing techniques and intelligent braille recognition, potentially finding applications in the fields of smart medical care and intelligent robotics. 

# Appendix A: Principles of FRR and PDH method

The fundamental reflective FRR structure consists of three key components: a straight waveguide, a ring-shaped optical waveguide, and a directional coupler. As shown in Fig. 9, light is launched into the straight waveguide at port 1. Upon reaching the directional coupler, a portion of the light is coupled into the ring cavity via port 4, while the remaining light continues propagating through the straight waveguide and exits at port 3. The coupled light propagates around the ring and re-enters the coupler at port 2. Here, a second partial coupling occurs, directing a portion of the light back into the straight waveguide for output at port 3, with the remaining portion continuing to circulate within the ring cavity. The transmission characteristics of each port of the FRR can be analyzed using the transmission matrix. 

本研究提出的结合机器学习的方法在实现准确快速的盲文识别方面具有独特优势。其识别准确率优于其他传感器与算法组合。通过对更广泛的词汇和句子进行网络训练，无需个人费力学习盲文规则即可实现完整的翻译功能。

# 5. 结论

本研究提出了一种采用柔性光纤环形谐振器（FRR）进行盲文识别的光纤触觉传感系统，其中FRR通过3D打印模具封装在PDMS溶液中，形成柔性光学皮肤。采用PDH光学锁频技术解调触觉压力，将频率波动转换为电压偏移。通过实验验证了压力响应性能：通过对传感器及闭环系统参数的理论分析与优化，实现了高精度快速测量。PDH解调曲线呈现陡峭线性斜率，使传感系统具备高灵敏度与高分辨率。系统PDH误差信号的线性区域延伸至约 $5 5 \mathrm { m V }$ ，对应0至3 N的触觉压力范围。通过调节闭环PDH系统参数，触觉压力平均响应时间缩短至0.1秒以下，满足盲文阅读的快速动态响应需求。进一步，该系统结合仿生滑动策略与人工智能技术实现连续盲文字符识别。为通过触觉压力反馈有效解码盲文点阵，在谐振器上固定三个不同硬度的小凸起以传递差异化压力。采用多层感知器神经网络完整区分了由三个点构成的八种排列组合，分类准确率达 $9 8 . 5 7 \%$ 。因此，当传感器滑过盲文板时，所有包含字母、数字及标点的盲文信息均可被解析。应用LSTM神经网络对5个单词产生的时序信号进行分类， $1 0 0 \%$ 的分类准确率表明即使单列识别存在微小误差，也不会影响盲文转码。该光纤触觉传感系统利用高品质因数FRR与PDH解调方法，实现了对常规盲文点的触觉压力分辨，有效区分八种不同盲文排列。进而借助机器学习算法完成盲文信息的精准转码，有效克服误差因素影响。基于柔性光学FRR的仿生触觉传感器研究将进一步推动触觉传感技术与智能盲文识别的进步，有望在智慧医疗与智能机器人领域获得应用。

# 附录A：FRR与PDH方法原理

基本反射式FRR结构由三个关键部分组成：直波导、环形光波导和定向耦合器。如图9所示，光从端口1注入直波导。当光到达定向耦合器时，一部分光通过端口4耦合进环形腔，剩余光则继续沿直波导传播并从端口3输出。耦合进环形腔的光沿环路传播后，从端口2重新进入耦合器。此时发生第二次部分耦合，一部分光被导回直波导并从端口3输出，剩余部分则继续在环形腔内循环。FRR各端口的传输特性可通过传输矩阵进行分析。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/e966fbd5627249585c3033e932e584aaedb3d82e86e3c7b7375f96c930a895a9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/63fa434c7ad1b91d721a1030e7532d93ddf674d80cf3eeadef177efa2c617594.jpg)



Fig. 9. Schematic diagram of fiber ring resonator (a) and equivalent FP cavity(b)


$$
\left[ \begin{array}{l} E _ {3} \\ E _ {4} \end{array} \right] = \sqrt {1 - \gamma} \left[ \begin{array}{c c} \sqrt {1 - k} & j \sqrt {k} \\ j \sqrt {k} & \sqrt {1 - k} \end{array} \right] \left[ \begin{array}{l} E _ {1} \\ E _ {2} \end{array} \right] \tag {4}
$$

$$
E _ {2} = e ^ {- \alpha_ {L}} e ^ {j \beta L} E _ {4}
$$

where, $E _ { i }$ $( i = 1 , 2 , 3 , 4 )$ respectively denotes each port of the FRR, $\gamma$ is the insertion loss of the directional coupler, $k$ γis the power coupling coefficient of the directional coupler, $\alpha _ { L }$ and $\beta L$ α βis the transmission loss and the phase change respectively through the optical fiber. When the light satisfies the phase-matching condition: $\beta L = 2 \pi$ , after propagating one round trip within the ring cavity, it undergoes constructive interference with the light at the through port, leading to confinement within the cavity. FRR is a typical multi-beam interferometer and its transmission spectrum exhibits sharp absorption peaks the resonance condition can be concluded: 

$$
n _ {\text {e f f}} \frac {L}{\lambda} = q \tag {5}
$$

where, $n _ { e f f }$ is the effective refractive index of optical fiber, $L$ is the length of the resonator, $\lambda$ is the wavelength, and $q$ is a positive integer. 

The PD output signal comprises a superposition of harmonics arising from the modulation frequency. However, the signal of interest, containing the resonant cavity sensing information, is masked by these harmonic noises. Consequently, correlation detection techniques are employed to extract the desired signal. The lock-in amplifier (LIA) is a specific type of correlation detector, utilizing a multiplier and a low-pass filter to achieve this [31,32]. The detailed processes of the modulation and demodulation within a LIA are as follows. 

The electric field of the incident light undergoes phase modulation and its electric field expression can be effectively expanded using the Jacobi-Anger expansion. When the modulation depth is small, the limited modulation depth confines the majority of the optical power within the carrier and the first-order sidebands. Consequently, the interaction with the resonator can be approximated as the simultaneous illumination by three distinct beams: the central carrier and 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/15462e7f28fa661ea6f333f8b4a9e543a06350badaddf4a6cbe9c38f4b32d6b7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-03-31/741742a7-4e28-475b-b542-3dc97fb6b0b6/c5343516fc0e8a9893cbdc0f4615057d31126f110cdc30cd2f8b5d86610e9eaf.jpg)



图9. 光纤环形谐振腔示意图(a)与等效FP腔示意图(b)


$$
\left[ \begin{array}{l} E _ {3} \\ E _ {4} \end{array} \right] = \sqrt {1 - \gamma} \left[ \begin{array}{c c} \sqrt {1 - k} & j \sqrt {k} \\ j \sqrt {k} & \sqrt {1 - k} \end{array} \right] \left[ \begin{array}{l} E _ {1} \\ E _ {2} \end{array} \right] \tag {4}
$$

$$
E _ {2} = e ^ {- \alpha_ {L}} e ^ {j \beta L} E _ {4}
$$

其中， $E _ { i }$ (i = 1、2、3、4)分别表示FRR的各个端口， 为定向耦合器的插入损耗，k为定向耦合器的功率耦合系数， $\alpha _ { L }$ 和 L分别为光纤的传输损耗和相位变化。当光满足相位匹配条件： $\beta L = 2 \pi$ 时，在环形腔内传播一个往返后，会与直通端口的光发生相长干涉，从而被限制在腔内。FRR是一种典型的多光束干涉仪，其透射光谱呈现尖锐的吸收峰，共振条件可归纳为：

$$
n _ {\text {e f f}} \frac {L}{\lambda} = q \tag {5}
$$

其中， $n _ { e f f }$ 是光纤的有效折射率， $L$ 是谐振腔的长度， $\lambda$ 是波长，而 $q$ 是一个正整数。

PD输出信号包含由调制频率产生的谐波叠加。然而，包含谐振腔传感信息的信号被这些谐波噪声所掩盖。因此，采用相关检测技术来提取所需信号。锁相放大器（LIA）是一种特定类型的相关检测器，利用乘法器和低通滤波器实现这一功能[31,32]。LIA内部调制与解调的详细过程如下。

入射光的电场经历相位调制，其电场表达式可利用雅可比-安格尔展开进行有效展开当调制深度较小时，有限的调制深度将大部分光功率限制在载波和一阶边带内。因此，与谐振腔的相互作用可近似为三个独立光束的同时照射：中心载波与

the two neighboring first-order sidebands. 

$$
\begin{array}{l} E _ {i n} = E _ {0} e ^ {j [ 2 \pi (f _ {0} + f _ {P Z T}) t + M \sin 2 \pi f _ {m} t + \phi_ {0} ]} \\ = E _ {0} e ^ {j [ 2 \pi (f _ {0} + f _ {P Z T}) t + \phi_ {0} ]} \sum_ {n = - 1} ^ {+ 1} J _ {n} (M) e ^ {j (n 2 \pi f _ {m} t)} \\ = E _ {0} \left\{J _ {0} (M) e ^ {j [ 2 \pi \left(f _ {0} + f _ {P Z T}\right) t + \phi_ {0} ]} + J _ {1} (M) e ^ {j [ 2 \pi \left(f _ {0} + f _ {P Z T} + f _ {m}\right) t + \phi_ {0} ]} \right. \tag {6} \\ + J _ {- 1} (M) e ^ {j [ 2 \pi (f _ {0} + f _ {P Z T} - f _ {m}) t + \phi_ {0} ]} \} \\ \end{array}
$$

where, $E _ { 0 }$ is the amplitude of the incident light, $f _ { 0 }$ is the initial center output frequency of the laser, $f _ { P Z T }$ is the speed of PZT frequency modulation, $M$ is the modulation coefficient, which can be calculated by $\begin{array} { r } { \dot { M } = \pi \frac { V _ { m } } { V _ { \pi } } } \end{array}$ , $V _ { m }$ and $f _ { m }$ are depth and frequency respectively of phase modulation, $V _ { \pi }$ πdenote the half-wave voltage of the EOM, $\phi _ { 0 }$ is the initial phase. 

π ϕIt is the first harmonic signal of the modulation frequency that functions as the signal to be demodulated only remaining the DC term and the first harmonic signal, because they encapsulate the information of phase change of the resonator. The electric field of the emergent light is the superposition of each carrier component and can be expressed as: 

$$
\begin{array}{l} E _ {o u t} = E _ {0} \left\{h _ {0} J _ {0} (M) e ^ {j \left[ 2 \pi \left(f _ {0} + f _ {P Z T}\right) t + \phi_ {0} \right]} e ^ {j \Phi_ {0}} \right. \\ + h _ {1} J _ {1} (M) e ^ {j [ 2 \pi (f _ {0} + f _ {P Z T} + f _ {m}) t + \phi_ {0} ]} e ^ {j \Phi_ {1}} \tag {7} \\ + h _ {- 1} J _ {- 1} (M) e ^ {j [ 2 \pi (f _ {0} + f _ {P Z T} - f _ {m}) t + \phi_ {0} ]} e ^ {j \Phi_ {- 1}} \} \\ \end{array}
$$

where, $h _ { n }$ and $\Phi _ { n }$ represent the amplitude transfer coefficient and phase transfer coefficient respectively. 

The PD output power contains intermodulation products arising from the mixing of three waves with distinct frequencies. We are particularly interested in the terms generated by the interference between the carrier and the first-order sidebands, as these terms encode phase demodulation information crucial for resonator characterization. A lock-in amplifier is employed to demodulate the desired signal from the complex PD output. This instrument, consisting of a multiplier, a LPF, and a phase shifter, offers a robust technique for extracting weak signals buried in noise. The PD output is first multiplied by a reference signal within the multiplier. Subsequently, the LPF removes high-frequency components, resulting in a DC output that is in phase with the frequency shift signal of the resonator. By adjusting the phase of the reference signal using the phase shifter, the lock-in amplifier output can be maximized, enhancing the signal-to-noise ratio and facilitating accurate demodulation. The output signal of the LIA can be summarized as: 

$$
V _ {f i l} = R _ {p d} I _ {0} \left(A _ {1} \sin \theta - B _ {1} \cos \theta\right) \tag {8}
$$

Near the resonance frequency, the response curve exhibits near-linearity. This characteristic allows the slope of this linear region to be effectively captured by the zero-point slope: 

$$
k _ {0} = \left. \frac {d V _ {f i l}}{d \Delta f} \right| _ {\Delta f = 0} \tag {9}
$$

where $\Delta f$ is the frequency offset between the laser and the resonator. 

# Appendix B: MLP neural network and LSTM model

The output value of the neuron in the neural network can be expressed by the following equation: 

$$
y = \max  \left(0, \omega^ {T} X + b\right) \tag {10}
$$

where $X$ is the input value, $\omega ^ { T }$ and $^ b$ are weights and biases respectively. 

两个相邻的一阶边带。

$$
\begin{array}{l} E _ {i n} = E _ {0} e ^ {j [ 2 \pi (f _ {0} + f _ {P Z T}) t + M \sin 2 \pi f _ {m} t + \phi_ {0} ]} \\ = E _ {0} e ^ {j [ 2 \pi (f _ {0} + f _ {P Z T}) t + \phi_ {0} ]} \sum_ {n = - 1} ^ {+ 1} J _ {n} (M) e ^ {j (n 2 \pi f _ {m} t)} \\ = E _ {0} \left\{J _ {0} (M) e ^ {j [ 2 \pi \left(f _ {0} + f _ {P Z T}\right) t + \phi_ {0} ]} + J _ {1} (M) e ^ {j [ 2 \pi \left(f _ {0} + f _ {P Z T} + f _ {m}\right) t + \phi_ {0} ]} \right. \tag {6} \\ + J _ {- 1} (M) e ^ {j [ 2 \pi (f _ {0} + f _ {P Z T} - f _ {m}) t + \phi_ {0} ]} \} \\ \end{array}
$$

其中， $E _ { 0 }$ 为入射光振幅， $f _ { 0 }$ 为激光器初始中心输出频率，fPZT为PZT调频速度， $M$ 为调制系数，可通过 $\begin{array} { r } { M = \pi \frac { V _ { m } } { V _ { \pi } } ] } \end{array}$ 计算得出， $V _ { m }$ 和 $f _ { m }$ 分别为相位调制的深度与频率， $V _ { \pi }$ 表示EOM的半波电压， $\phi _ { 0 }$ π为初始相位。

它是调制频率的一次谐波信号，作为待解调信号，仅保留直流项和一次谐波信号，因为它们包含了谐振器相位变化的信息。出射光的电场是各载波分量的叠加，可以表示为：

$$
\begin{array}{l} E _ {o u t} = E _ {0} \left\{h _ {0} J _ {0} (M) e ^ {j \left[ 2 \pi \left(f _ {0} + f _ {P Z T}\right) t + \phi_ {0} \right]} e ^ {j \Phi_ {0}} \right. \\ + h _ {1} J _ {1} (M) e ^ {j [ 2 \pi \left(f _ {0} + f _ {P Z T} + f _ {m}\right) t + \phi_ {0} ]} e ^ {j \Phi_ {1}} \tag {7} \\ + h _ {- 1} J _ {- 1} (M) e ^ {j \left[ 2 \pi \left(f _ {0} + f _ {P Z T} - f _ {m}\right) t + \phi_ {0} \right]} e ^ {j \Phi_ {- 1}} \rbrace \\ \end{array}
$$

其中， $h _ { n }$ 和 $\Phi _ { n }$ 分别代表振幅传递系数和相位传递系数。

PD输出功率包含由三个不同频率波混合产生的互调产物。我们特别关注载波与一阶边带之间干涉产生的项，因为这些项编码了对谐振器表征至关重要的相位解调信息。锁相放大器被用于从复杂的PD输出中解调出所需信号。该仪器由乘法器、低通滤波器和移相器组成，为提取淹没在噪声中的微弱信号提供了稳健的技术。PD输出首先在乘法器中与参考信号相乘，随后低通滤波器去除高频分量，产生与谐振器频移信号同相的直流输出。通过移相器调节参考信号的相位，可使锁相放大器输出最大化，从而提升信噪比并实现精确解调。锁相放大器的输出信号可归纳为：

$$
V _ {f i l} = R _ {p d} I _ {0} \left(A _ {1} \sin \theta - B _ {1} \cos \theta\right) \tag {8}
$$

在共振频率附近，响应曲线呈现近似线性特性。这一特性使得该线性区域的斜率能够通过零点斜率有效捕捉：

$$
k _ {0} = \left. \frac {d V _ {f i l}}{d \Delta f} \right| _ {\Delta f = 0} \tag {9}
$$

其中∆f是激光与谐振器之间的频率偏移。

附录B：MLP神经网络与LSTM模型

神经网络的输出值 神经网络中的神经元可以用以下公式表示 评估：

$$
y = \max  \left(0, \omega^ {T} X + b\right) \tag {10}
$$

其中 $X$ 是输入值， $\omega ^ { T }$ 和 $^ b$ 分别是权重和偏置。

The network parameters are updated using the backpropagation algorithm, resulting in the formation of the MLP neural network. This network establishes a nonlinear mapping between the input tactile signals and the output target dot arrangements. The output value of the neuron in the LSTM can be expressed by the following equation: 

$$
h _ {t} = O _ {t} \tanh  \left(f _ {t} C _ {t - 1} + i _ {t} C _ {t}\right) \tag {11}
$$

where $f _ { t } , i _ { t }$ , and $O _ { t }$ represent the forget gate, input gate and output gate of the LSTM model. The update of the neural network parameters can be expressed using the following equation: 

$$
\omega_ {\text {n e w}} = \omega_ {\text {o l d}} - \eta \nabla E (\omega) \tag {12}
$$

$$
b _ {n e w} = b _ {o l d} - \eta \nabla E (b)
$$

where $\eta$ is the learning rate, ∇ represents the gradient operator. 

Funding. National Key Research and Development Program of China (2022YFE0140400); National Natural Science Foundation of China (62405027); Scientific Research Project of Liaoning Provincial Education Department (LJKMZ 20220544). 

Disclosures. The authors declare no conflicts of interest. 

Data availability. Data underlying the results presented in this paper are not publicly available at this time but may be obtained from the authors upon reasonable request. 

# References



1. J. Wang, X. Liu, R. Li, et al., “Biomimetic strategies and technologies for artificial tactile sensory systems,” Trends Biotechnol. 41(7), 951–964 (2023). 





2. Y. Li, M. Zhao, and Y. Yan et al., “Multifunctional biomimetic tactile system via a stick-slip sensing strategy for human–machine interactions,” npj Flexible Electron. 6(1), 46 (2022). 





3. T. Kim, I. Hong, and M. Kim et al., “Ultra-stable and tough bioinspired crack-based tactile sensor for small legged robots,” npj Flexible Electron. 7(1), 22 (2023). 





4. A. L. Trejos, J. Jayender, and M. Perri et al., “Robot-assisted tactile sensing for minimally invasive tumor localization,” The International Journal of Robotics Research 28(9), 1118–1133 (2009). 





5. S. Li, X. Chen, and X. Li et al., “Bioinspired robot skin with mechanically gated electron channels for sliding tactile perception,” Sci. Adv. 8(48), eade0720 (2022). 





6. H. Oh, G.-C. Yi, M. Yip, et al., “Scalable tactile sensor arrays on flexible substrates with high spatiotemporal resolution enabling slip and grip for closed-loop robotics,” Sci. Adv. 6(46), eabd7795 (2020). 





7. N. Bai, Y. Xue, and S. Chen et al., “A robotic sensory system with high spatiotemporal resolution for texture recognition,” Nat. Commun. 14(1), 7121 (2023). 





8. Y. Yan, Z. Hu, and Z. Yang et al., “Soft magnetic skin for super-resolution tactile sensing with force self-decoupling,” Sci. Robot. 6(51), eabc8801 (2021). 





9. S. Isayed and R. Tahboub, “A review of optical braille recognition,” in 2015 2nd World Symposium on Web Applications and Networking (WSWAN), (IEEE, 2015), pp. 1–6. 





10. B.-S. Park, S.-M. Im, and H. Lee et al., “Visual and tactile perception techniques for braille recognition,” Micro and Nano Syst Lett 11(1), 23 (2023). 





11. P. Potdar, D. Hardman, E. Almanzor, et al., “High-speed tactile braille reading via biomimetic sliding interactions,” IEEE Robot. Autom. Practice 1, 1 (2024). 





12. X.-F. Zhao, C.-Z. Hang, and H.-L. Lu et al., “A skin-like sensor for intelligent braille recognition,” Nano Energy 68, 104346 (2020). 





13. Z. Gao, L. Chang, and B. Ren et al., “Enhanced braille recognition based on piezoresistive and piezoelectric dual-mode tactile sensors,” Sens. Actuators, A 366, 115000 (2024). 





14. Y. Lu, D. Kong, and G. Yang et al., “Machine learning-enabled tactile sensor design for dynamic touch decoding,” Adv. Sci. 10(32), 2303949 (2023). 





15. L. Huang, B. Luo, and X. Zou et al., “Research on efficient braille recognition based on the pair-u-shaped micro-nano optical fiber fingerprint-like tactile sensors,” Optics Laser Technology 179, 111349 (2024). 





16. A. Prasad, S. Sebastian, and S. Asokan, “Diaphragm-micro-stylus-based fiber bragg grating tactile sensor,” IEEE Sens. J. 20(12), 6394–6399 (2020). 





17. N. Yao, X. Wang, and S. Ma et al., “Single optical microfiber enabled tactile sensor for simultaneous temperature and pressure measurement,” Photonics Res. 10(9), 2040–2046 (2022). 





18. Z. Wang, Z. Chen, and L. Ma et al., “Optical microfiber intelligent sensor: wearable cardiorespiratory and behavior monitoring with a flexible wave-shaped polymer optical microfiber,” ACS Appl. Mater. Interfaces 16(7), 8333–8345 (2024). 



网络参数通过反向传播算法进行更新，从而形成了MLP神经网络。该网络在输入触觉信号与输出目标点阵排列之间建立了非线性映射关系。LSTM中神经元的输出值可由以下公式表示：

$$
h _ {t} = O _ {t} \tanh  \left(f _ {t} C _ {t - 1} + i _ {t} C _ {t}\right) \tag {11}
$$

其中ft、it和 $O _ { \imath }$ t分别代表LSTM模型中的遗忘门、输入门和输出门。神经网络参数的更新可通过以下公式表示：

$$
\omega_ {\text {n e w}} = \omega_ {\text {o l d}} - \eta \nabla E (\omega) \tag {12}
$$

$$
b _ {n e w} = b _ {o l d} - \eta \nabla E (b)
$$

其中 $\eta$ 是学习率，∇ 代表梯度算子

r。 

资助项目。国家重点研发计划（2022YFE0140400）；国家自然科学基金（62405027）；辽宁省教育厅科学研究项目（LJKMZ 20220544）。

披露事项。作者声明无利益冲突。

数据可用性。本文结果所依据的数据目前尚未公开，但可根据合理请求向作者索取。

# 参考文献

1. J. Wang, X. Liu, R. Li, et al., “面向人工触觉传感系统的仿生策略与技术，” Trends Biotechnol. 41(7), 951–964 (2023).2. Y. Li, M. Zhao, Y. Yan 等, “基于粘滑传感策略用于人机交互的多功能仿生触觉系统，” npj Flexible Electron. 6(1), 46 (2022).3. T. Kim, I. Hong, M. Kim 等, “用于小型腿式机器人的超稳定、高韧性仿生裂纹触觉传感器，” npj Flexible Electron. 7(1), 22 (2023).4. A. L. Trejos, J. Jayender, M. Perri 等, “机器人辅助触觉传感用于微创肿瘤定位，” The International Journal of Robotics Research 28(9), 1118–1133 (2009).5. S. Li, X. Chen, X. Li 等, “具有机械门控电子通道用于滑动触觉感知的仿生机器人皮肤，” Sci. Adv. 8(48), eade0720 (2022).6. H. Oh, G.-C. Yi, M. Yip, et al., “柔性基底上具有高时空分辨率、可实现机器人闭环抓取与防滑的可扩展触觉传感器阵列，” Sci. Adv. 6(46), eabd7795 (2020).7. N. Bai, Y. Xue, S. Chen 等, “用于纹理识别的高时空分辨率机器人传感系统，” Nat. Commun. 14(1), 7121 (2023).8. Y. Yan, Z. Hu, Z. Yang 等, “用于具有力自解耦超分辨触觉感知的软磁皮肤，” Sci. Robot. 6(51), eabc8801 (2021).9. S. Isayed, R. Tahboub, “光学盲文识别综述，” 收录于 2015 2nd World Symposium on Web Applications and Networking (WSWAN), (IEEE, 2015), pp. 1–6.10.B.-S. Park, S.-M. Im, H. Lee 等, “用于盲文识别的视觉与触觉感知技术，” Micro and Nano Syst Lett 11(1), 23 (2023).11. P. Potdar, D. Hardman, E. Almanzor, et al., “通过仿生滑动交互实现高速触觉盲文阅读，” IEEE Robot. Autom. Practice 1, 1 (2024).12. X.-F. Zhao, C.-Z. Hang, H.-L. Lu 等, “用于智能盲文识别的类皮肤传感器，Nano Energy 68, 104346 (2020).13. Z. Gao, L. Chang, B. Ren 等, “基于压阻与压电双模触觉传感器的增强型盲文识别，” Sens. Actuators, A 366, 115000 (2024).14. Y. Lu, D. Kong, G. Yang 等, “用于动态触觉解码的机器学习赋能触觉传感器设计，” Adv. Sci. 10(32), 2303949 (2023).15. L. Huang, B. Luo, X. Zou 等, “基于对U形微纳光纤指纹状触觉传感器的高效盲文识别研究，” Optics Laser Technology 179, 111349 (2024).16. A. Prasad, S. Sebastian, S. Asokan, “基于膜片-微探针的光纤布拉格光栅触觉传感器，” IEEE Sens. J. 20(12), 6394–6399 (2020).17. N. Yao, X. Wang, S. Ma 等, “用于同步温度与压力测量的单根光学微纤维触觉传感器，” Photonics Res.10(9), 2040–2046 (2022).18. Z. Wang, Z. Chen, L. Ma 等, “光学微纤维智能传感器：基于柔性波浪形聚合物光学微纤维的可穿戴心呼吸与行为监测，” ACS Appl. Mater. Interfaces 16(7), 8333–8345 (2024).



19. K. Xiao, Z. Wang, and Y. Ye et al., “Pdms-embedded wearable fbg sensors for gesture recognition and communication assistance,” Biomed. Opt. Express 15(3), 1892–1909 (2024). 





20. X. Zhan, Z. Wang, and S. Kumar et al., “The application of pound-drever-hall technology in high resolution sensing-a review,” IEEE Sens. J. 23(7), 6427–6438 (2023). 





21. Q. Liu, S. Zhao, and Z. He, “Improved pound-drever-hall techniques for high resolution optical fiber grating sensors,” J. Lightwave Technol. 39(12), 3846–3854 (2021). 





22. X. Ma, Z. Cai, and C. Zhuang et al., “Integrated microcavity electric field sensors using pound-drever-hall detection,” Nat. Commun. 15(1), 1386 (2024). 





23. Y.-S. Jang, J. Lim, and W. Wang et al., “Measurement of sub-fm/hz 1/2 displacement spectral densities in ultrahigh-q single-crystal microcavities with hertz-level lasers,” Photonics Res. 10(5), 1202–1209 (2022). 





24. B. Culshaw and A. Kersey, “Fiber-optic sensing: A historical perspective,” J. Lightwave Technol. 26(9), 1064–1078 (2008). 





25. K. J. Vahala, “Optical microcavities,” Nature 424(6950), 839–846 (2003). 





26. L. Chen, S. Karilanova, and S. Chaki et al., “Spike timing–based coding in neuromimetic tactile system enables dynamic object classification,” Science 384(6696), 660–665 (2024). 





27. B. Shih, D. Shah, and J. Li et al., “Electronic skins and machine learning for intelligent soft robots,” Sci. Robot. 5(41), eaaz9239 (2020). 





28. I. Sutskever, O. Vinyals, and Q. V. Le, “Sequence to sequence learning with neural networks,” Advances in neural information processing systems 27, 1 (2014). 





29. S. F. Müller-Cleve, V. Fra, and L. Khacef et al., “Braille letter reading: A benchmark for spatio-temporal pattern recognition on neuromorphic hardware,” Front. Neurosci. 16, 951164 (2022). 





30. T. Li, A. Zhang, and M. Du et al., “A fingertip optical fiber composite sensor with conformal design for robotic perception of tactile force,” IEEE/ASME Transactions on Mechatronics 1, 1 (2024). 





31. E. D. Black, “An introduction to pound–drever–hall laser frequency stabilization,” Am. J. Phys. 69(1), 79–87 (2001). 





32. W. Liang, V. S. Ilchenko, and A. A. Savchenkov et al., “Resonant microphotonic gyroscope,” Optica 4(1), 114–117 (2017). 





19. K. Xiao, Z. Wang, and Y. Ye 等人，“用于手势识别与交流辅助的PDMS嵌入式可穿戴FBG传感器，” Biomed. Opt. Express 15(3), 1892–1909 (2024).20. X. Zhan, Z. Wang, and S. Kumar 等人，“Pound-Drever-Hall技术在高分辨率传感中的应用综述，” IEEE Sens. J. 23(7), 6427–6438 (2023).21. Q. Liu, S. Zhao, and Z. He，“用于高分辨率光纤光栅传感器的改进型Pound-Drever-Hall技术，” J. Lightwave Technol. 39(12), 3846–3854 (2021).22.X. Ma, Z. Cai, and C. Zhuang 等人，“采用Pound-Drever-Hall检测的集成微腔电场传感器，” Nat. Commun. 15(1), 1386 (2024).23. Y.-S. Jang, J. Lim, and W. Wang 等人，“使用赫兹级激光器在超高Q值单晶微腔中测量亚fm/${ \mathrm { H z } } ^ { \wedge } \{ 1 / 2 \}$ 位移谱密度，” Photonics Res. 10(5), 1202–1209 (2022).24. B. Culshaw and A. Kersey，“光纤传感：历史视角，” J. Lightwave Technol. 26(9), 1064–1078 (2008).25. K. J. Vahala，“光学微腔，” Nature 424(6950), 839–846 (2003).26. L. Chen, S. Karilanova, and S. Chaki 等人，“基于脉冲时序编码的神经拟态触觉系统实现动态物体分类，” Science 384(6696), 660–665 (2024).27. B. Shih, D. Shah, and J. Li 等人，“用于智能软体机器人的电子皮肤与机器学习，” Sci. Robot. 5(41), eaaz9239 (2020).28. I. Sutskever, O. Vinyals, and Q. V. Le，“使用神经网络的序列到序列学习，” Advances in neural information processing systems 27, 1 (2014).29. S. F. Müller-Cleve, V. Fra, and L. Khacef 等人，“盲文字母阅读：神经形态硬件上时空模式识别的基准，” Front. Neurosci. 16, 951164 (2022).30. T. Li, A. Zhang, and M. Du 等人，“用于机器人触觉力感知的共形设计指尖光纤复合传感器，” IEEE/ASME Transactions on Mechatronics 1, 1 (2024).31. E. D. Black，“Pound–Drever–Hall激光稳频技术简介，” Am. J. Phys. 69(1), 79–87 (2001).32. W. Liang, V. S. Ilchenko, and A. A. Savchenkov 等人，“谐振微光子陀螺仪，” Optica 4(1), 114–117 (2017).

