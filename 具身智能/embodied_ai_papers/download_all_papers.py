#!/usr/bin/env python3
"""
具身智能论文批量下载脚本
为叶哲昊定制的论文下载工具

使用方法：
    python download_all_papers.py

要求：Python 3.6+, requests库 (pip install requests)
"""

import requests
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# 论文列表: (文件名, arXiv ID, 子目录)
PAPERS = [
    # 01_Surveys - 5篇
    ("Embodied_AI_Survey_ZJU", "2407.06886", "01_Surveys"),
    ("VLA_Survey_2024", "2405.14093", "01_Surveys"),
    ("VLA_Concepts_Progress_2025", "2505.04769", "01_Surveys"),
    ("World_Models_Survey_2025", "2510.16732", "01_Surveys"),
    ("6D_Pose_Survey_2024", "2405.07801", "01_Surveys"),
    
    # 02_VLA_Core - 11篇
    ("RT1_Robotics_Transformer", "2212.06817", "02_VLA_Core"),
    ("RT2_VLA_Model", "2307.15818", "02_VLA_Core"),
    ("Pi0_Flow_Model", "2410.24164", "02_VLA_Core"),
    ("OpenVLA_Open_Source", "2406.09246", "02_VLA_Core"),
    ("GROOT_N1_NVIDIA", "2503.14734", "02_VLA_Core"),
    ("RDT_Diffusion_Transformer", "2410.07864", "02_VLA_Core"),
    ("Octo_Generalist_Policy", "2405.12213", "02_VLA_Core"),
    ("3D_VLA_World_Model", "2403.09631", "02_VLA_Core"),
    ("GeoVLA_3D_Representation", "2508.09071", "02_VLA_Core"),
    ("TraceVLA_Temporal_Awareness", "2412.10345", "02_VLA_Core"),
    ("SpatialVLM_Spatial_Reasoning", "2401.12125", "02_VLA_Core"),
    
    # 03_Imitation_Learning - 5篇
    ("ACT_Action_Chunking", "2304.13705", "03_Imitation_Learning"),
    ("Diffusion_Policy", "2303.04137", "03_Imitation_Learning"),
    ("Diffusion_Transformer_Policy", "2410.15959", "03_Imitation_Learning"),
    ("Aloha_Unleashed", "2410.13126", "03_Imitation_Learning"),
    ("Open_X_Embodiment", "2310.08864", "03_Imitation_Learning"),
    
    # 04_6D_Pose - 7篇
    ("MegaPose_Render_Compare", "2212.06870", "04_6D_Pose"),
    ("FoundationPose_Unified", "2312.08344", "04_6D_Pose"),
    ("SAM_6D_Zero_Shot", "2311.15707", "04_6D_Pose"),
    ("Any6D_Model_Free", "2503.18673", "04_6D_Pose"),
    ("GCE_Pose_Category_Level", "2502.04293", "04_6D_Pose"),
    ("6DOPE_GS_Gaussian_Splatting", "2412.01543", "04_6D_Pose"),
    ("YOLO_6D_Pose", "2312.10497", "04_6D_Pose"),
    
    # 05_World_Models - 4篇
    ("GWM_Gaussian_World_Model", "2503.09631", "05_World_Models"),
    ("GAF_Gaussian_Action_Field", "2506.14135", "05_World_Models"),
    ("3D_Diffusion_Policy", "2403.03954", "05_World_Models"),
    ("Robo_GS_Gaussian_Splatting", "2502.15194", "05_World_Models"),
    
    # 06_Tactile_Multimodal - 3篇
    ("Tactile_VLA_Physical", "2507.09160", "06_Tactile_Multimodal"),
    ("VLA_Touch_Tactile", "2507.17294", "06_Tactile_Multimodal"),
    ("Physically_Grounded_Multimodal", "2511.01210", "06_Tactile_Multimodal"),
]


def download_paper(name, arxiv_id, folder, base_dir="."):
    """下载单篇论文，带重试机制"""
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    folder_path = os.path.join(base_dir, folder)
    filepath = os.path.join(folder_path, f"{name}.pdf")
    
    # 已存在且大小正常则跳过
    if os.path.exists(filepath) and os.path.getsize(filepath) > 10000:
        return True, f"[SKIP] {name} (已存在)"
    
    os.makedirs(folder_path, exist_ok=True)
    
    # 最多重试3次
    for attempt in range(3):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            with requests.get(url, headers=headers, stream=True, timeout=60) as r:
                r.raise_for_status()
                with open(filepath, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=64*1024):
                        if chunk:
                            f.write(chunk)
            
            size = os.path.getsize(filepath)
            if size > 10000:
                return True, f"[OK] {name} ({size//1024}KB)"
            else:
                os.remove(filepath)
                return False, f"[FAIL] {name} (文件太小)"
                
        except Exception as e:
            if attempt < 2:
                time.sleep(2)
                continue
            return False, f"[FAIL] {name} ({str(e)[:50]})"
    
    return False, f"[FAIL] {name} (重试耗尽)"


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print("=" * 60)
    print("具身智能论文批量下载工具")
    print(f"共 {len(PAPERS)} 篇论文")
    print("=" * 60)
    
    success = 0
    failed = 0
    skipped = 0
    
    # 使用3线程并发下载
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {
            executor.submit(download_paper, name, aid, folder, base_dir): (name, aid, folder)
            for name, aid, folder in PAPERS
        }
        
        for future in as_completed(futures):
            ok, msg = future.result()
            print(msg)
            if ok and "SKIP" in msg:
                skipped += 1
            elif ok:
                success += 1
            else:
                failed += 1
                # 失败时等1秒再下一个
                time.sleep(1)
    
    print("=" * 60)
    print(f"下载完成: 成功 {success} 篇, 跳过 {skipped} 篇, 失败 {failed} 篇")
    print("=" * 60)
    
    if failed > 0:
        print("\n提示: 失败的论文可以重新运行此脚本重试")
        print("      已下载的论文会自动跳过")


if __name__ == "__main__":
    main()
