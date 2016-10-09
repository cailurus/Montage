# Montage: A multi-pattern matching toolkit

Montage 是一个多模匹配的工具库，包含有经典的 [WuManber 多模匹配](http://webglimpse.net/pubs/TR94-17.pdf) 和 [AC 自动机](https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm) 的高效 C 实现，并使用 Python 进行 API 的简易封装。

## Performance

## Getting started

```python
from tmontage import Montage

# let name this Montage
sample = Montage("monster_sample")

# init your monster
sample.init_pattern(['蓝天', '白云'])

# search
sample.search_text('蓝天下有朵朵白云')
```

## How to get
`pip install tmontage`
