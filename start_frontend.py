#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DataMasker前端启动脚本
"""

import os
import sys
import subprocess
import time

def check_node_installed():
    """检查Node.js是否已安装"""
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Node.js已安装: {result.stdout.strip()}")
            return True
        else:
            print("❌ Node.js未安装或未正确配置")
            return False
    except FileNotFoundError:
        print("❌ Node.js未安装")
        print("请访问 https://nodejs.org/ 下载并安装Node.js")
        return False

def check_npm_installed():
    """检查npm是否已安装"""
    try:
        result = subprocess.run(['npm', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ npm已安装: {result.stdout.strip()}")
            return True
        else:
            print("❌ npm未安装或未正确配置")
            return False
    except FileNotFoundError:
        print("❌ npm未安装")
        return False

def check_dependencies():
    """检查前端依赖是否已安装"""
    if not os.path.exists('node_modules'):
        print("📦 正在安装前端依赖...")
        try:
            subprocess.run(['npm', 'install'], check=True)
            print("✅ 前端依赖安装完成")
        except subprocess.CalledProcessError as e:
            print(f"❌ 依赖安装失败: {e}")
            return False
    else:
        print("✅ 前端依赖已安装")
    
    return True

def start_frontend():
    """启动前端服务"""
    print("🚀 正在启动DataMasker前端服务...")
    
    # 检查Node.js
    if not check_node_installed():
        return False
    
    # 检查npm
    if not check_npm_installed():
        return False
    
    # 检查依赖
    if not check_dependencies():
        return False
    
    # 启动前端服务
    try:
        print("📍 前端服务将在 http://localhost:9528 启动")
        print("📍 后端服务地址: http://0.0.0.0:12345")
        print("🔄 正在启动前端服务...")
        
        # 使用npm启动开发服务器
        process = subprocess.Popen(['npm', 'run', 'dev'])
        
        print("✅ 前端服务已启动")
        print("按 Ctrl+C 停止服务")
        
        # 等待进程结束
        process.wait()
        
    except KeyboardInterrupt:
        print("\n🛑 正在停止服务...")
        if 'process' in locals():
            process.terminate()
        print("✅ 服务已停止")
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        return False
    
    return True

if __name__ == '__main__':
    start_frontend()

