
LargeLangugeModel:
    -llama

Embedding:  
    - sentence-transformers/all-MiniLM-L6-v2

FrameWork:
    - Groq 

Prompting:
    Prephase:
        -   Zero Short Prompting




**💥 SingletoneMeta Understanding Diagrom:**

               ┌────────────────────┐
               │       type         │  (Parent of all metaclasses)
               └────────────────────┘
                        ▲
                        │
               ┌────────────────────┐
               │  SingletonMeta     │  (Child of `type`, overrides `__call__()`)
               └────────────────────┘
                        ▲
                        │
               ┌────────────────────┐
               │      MyClass       │  (Uses SingletonMeta as metaclass)
               └────────────────────┘
                        ▲
                        │
               ┌────────────────────┐
               │      obj1, obj2    │  (Instances, but always the same!)
               └────────────────────┘
