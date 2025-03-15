# Agent Tools

提供LLM工具调用、响应解析和服务管理的组件集合。

## 安装

基本安装：
```bash
pip install git+https://github.com/biantaishabi2/wangbo-agent-tools.git
```

包含Gemini支持的安装：
```bash
pip install git+https://github.com/biantaishabi2/wangbo-agent-tools.git#egg=wangbo-agent-tools[gemini]
```

## 主要组件

- **llm_service**: LLM服务统一接口
- **parser**: LLM响应解析器
- **tool_manager**: 工具调用管理系统
- **tools**: 基础工具实现
- **task_analyzer**: 任务完成状态分析器
- **gemini_analyzer**: 基于Gemini的任务分析器
- **followup_generator**: 自动跟进问题生成器

## 使用示例

### 工具管理器和工具调用

```python
from agent_tools.tool_manager import ToolManager
from agent_tools.tools import APICallTool, ToolCallResult

# 创建工具管理器
tool_manager = ToolManager()

# 创建会话管理器（为API工具提供会话）
class SessionManager:
    def get_session(self):
        import requests
        return requests.Session()

# 创建和注册工具
session_manager = SessionManager()
api_tool = APICallTool(session_manager)
tool_manager.register_tool("api_call", api_tool)

# 执行工具调用
params = {
    "url": "https://httpbin.org/get",
    "method": "GET",
    "headers": {"Content-Type": "application/json"}
}
result = await tool_manager.execute_tool("api_call", params)
print(f"Success: {result.success}, Result: {result.result}")
```

### LLM服务

```python
from agent_tools.llm_service import LLMService

# 创建LLM服务回调函数
async def call_llm(prompt, system_prompt, messages, stream=False):
    # 实现LLM调用逻辑...
    return "这是LLM的回复"

# 创建LLM服务
llm_service = LLMService(
    call_llm=call_llm,
    roles={
        "default": {"system_prompt": "你是一个有帮助的助手。"},
        "coder": {"system_prompt": "你是一个编程专家。"}
    }
)

# 设置角色并发送请求
llm_service.current_role = "coder"
response = await llm_service.process_chat_request({"messages": [{"content": "如何用Python创建一个web服务器?"}]})
```

## 与AG2-Agent集成

参见AG2-Agent项目中的`ToolManagerAdapter`类，用于将agent_tools与AG2-Agent框架集成。