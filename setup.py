from setuptools import setup, find_packages

setup(
    name="wangbo-agent-tools",
    version="0.1.0",
    packages=["agent_tools"],
    install_requires=[
        "requests",
        # 条件依赖，Gemini分析器需要
        "google-generativeai;python_version>='3.8'",
    ],
    extras_require={
        "gemini": ["google-generativeai>=0.7.0"],
    },
    author="Wang Bo",
    description="Tools for AI agent integration",
    long_description="提供LLM工具调用、响应解析和服务管理的组件集合",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)