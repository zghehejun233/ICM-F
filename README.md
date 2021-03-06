# ICM-F

## 仓库规范（建议）

### 版本管理规范

项目代码release包括三类：

- 大版本(x.0.0)
- 小版本(x.x.0)
- 补丁(x.x.x)

### Git Commit代码提交规范

#### commit message格式

git commit 提交样式规范：

> : 
>
> 注意：冒号后面又空格

```
<类型>: <标题>
<空一行>
<内容>
```

#### 1.3.2 格式说明

##### <类型>

用于说明 commit 的类别(type)，只允许使用下面7个标识。

```
# 主要type
feat:     增加新功能
fix:      修复bug
data:     添加新数据

# 特殊type
docs:     只改动了文档相关的内容
style:    不影响代码含义的改动，例如去掉空格、改变缩进、增删分号
build:    构造工具的或者外部依赖的改动，例如webpack，npm
refactor: 代码重构时使用,重构（即不是新增功能，也不是修改bug的代码变动）
revert:   执行git revert打印的message

# 暂不使用type
test:     添加测试或者修改现有测试
perf:     提高性能的改动
ci:       与CI（持续集成服务）有关的改动
chore:    不修改src或者test的其余修改，例如构建过程或辅助工具的变动
```

当一次改动包括`主要type`与`特殊type`时，统一采用`主要type`。

##### <标题>

commit 目的的简短描述，不超过50个字符

##### <内容>

对本次 commit 的详细描述，可以分成多行，可详细说明代码变动的动机。

#### 示例

```
feat: 添加了xxx功能

对本次 commit 的详细描述，可以分成多行，可详细说明代码变动的动机
```

## 定义

### 八个参量

```python
import numpy as np

happiness_index = np.array([])
development_index = np.array([])
resource_index = np.array([])
labor_index = np.array([])
economic_index = np.array([])
education_index = np.array([])
technology_index = np.array([])
population = np.array([])
```

### 定义科技水平的两个子指标

patents_per_capitan = np.array([])
electricity_per_capitan = np.array([])

### 定义资源水平的三个子指标及其矩阵

population_density_per_city = np.array([])
water_per_capitan = np.array([])
forest_per_capitan = np.array([])

resource_matrix = np.array([])