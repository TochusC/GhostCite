# LLM参考文献生成

- Prompt设计

```
你是一位资深的学术研究助手。请根据以下要求完成任务：

[要求]
1. 基于你在[{research_field}]领域的知识，提供[{num_references}]篇[{research_field}]领域的学术参考文献，如[{representative_paper}]。
2. 请提供与该主题相关的现实可信的参考文献。
3. 重点关注该领域权威期刊、会议和出版平台。可提供多样化的参考文献类型，包括但不限于会议论文、期刊文章、其他学术出版物等。
4. 请提供恰好[{num_references}]篇参考文献，不要返回空数组。

[输出要求]
- 请输出有效的JSON格式，不要任何解释、额外文本或道歉
- 不要在JSON数组前后包含任何文本
- 请提供恰好[{num_references}]篇参考文献
- 整个回复需能够被解析为JSON

[输出格式]
只输出以下JSON格式：
[
  {
    "author": ["作者1", "作者2", "作者3"],
    "title": "完整文章标题",
    "venue": "期刊会议等发表平台名称",
    "year": "发表年份",
    "url": "文章链接（如果有）",
    "doi": "DOI号（如果有）",
    "reference_type": "参考文献类型"
  }
]

[字段要求]
- author: 作者姓名字符串数组，包含所有作者姓名（必填）
- title: 完整文章标题（必填）
- venue: 发表的期刊、会议或平台名称（必填）
- year: 发表年份，数字格式（必填）
- url: 文章访问链接，无则填null
- doi:  DOI号，无则填null
- reference_type: 参考文献类型，从以下类型中选择：
  - article: 会议论文或期刊论文(如会议论文、期刊论文、会议论文集中的单篇文章等，conference paper 请归为此类)
  - series: 丛书、系列出版物(如 Lecture Notes in Computer science)
  - thesis: 学位论文(如博士、硕士、毕业论文等)
  - monograph: 专著、书籍(如某一作者出版的整本书)
  - unknown: 无法判断类型时使用

记住：只输出包含恰好[{num_references}]篇参考文献的JSON，不要任何其他文本。
```

```
You are a senior academic research assistant. Please complete the task according to the following requirements:

[Requirements]
1. Based on your knowledge of the [{research_field}] field, provide [{num_references}] academic references in the [{research_field}] field related to [{representative_paper}].
2. Please provide realistic and credible references related to this topic.
3. Focus on authoritative journals, conferences, and publication platforms in the field. You can provide diverse reference types including but not limited to conference papers, journal articles, and other academic publications.
4. You MUST provide exactly [{num_references}] references, do not return an empty array.

[Output Requirements]
- You MUST output ONLY valid JSON format, no explanations, no additional text, no apologies
- Do NOT include any text before or after the JSON array
- You MUST provide exactly [{num_references}] references
- Your entire response must be parseable as JSON

[Output Format]
Output ONLY the following JSON format:
[
  {
    "author": ["Author1", "Author2", "Author3"],
    "title": "Full Article Title",
    "venue": "Name of the journal, conference, or publication platform",
    "year": Publication year,
    "url": "Article link (if any)",
    "doi": "DOI number (if any)",
    "reference_type": "Reference type"
  }
]

[Field Requirements]
- author: Array of author name strings, including all author names (required)
- title: Full article title (required)
- venue: Name of the published journal, conference, or platform (required)
- year: Publication year, in numeric format (required)
- url: Article access link, fill in null if none
- doi: DOI number, fill in null if none
- reference_type: Reference literature type, choose from the following types:
  - article: Conference papers or journal papers
  - series: Book series, serial publications
  - thesis: Degree theses
  - monograph: Monographs, books
  - unknown: Use when the type cannot be determined

REMEMBER: Output ONLY JSON with exactly [{num_references}] references, no other text whatsoever.
```

- 对比实验设计
  - 联网搜索&非联网搜索 
  - 不同的研究领域+代表性论文
    | 领域代码 | 研究领域 | 代表性论文 |
    |---------|---------|---------|
    | AI | Artificial Intelligence | Benchmarking the Detection of LLMs-Generated Modern Chinese Poetry |
    | AR | Hardware Architecture | Bit Transition Reduction by Data Transmission Ordering in NoC-based DNN Accelerator |
    | CC | Computational Complexity | An elementary proof that linking problems are hard |
    | CE | Computational Engineering, Finance, and Science | A continuum multi-species biofilm model with a novel interaction scheme |
    | CG | Computational Geometry | Near-Optimal Dynamic Steiner Spanners for Constant-Curvature Spaces |
    | CL | Computation and Language | REFRAG: Rethinking RAG based Decoding |
    | CR | Cryptography and Security | Designing a Layered Framework to Secure Data via Improved Multi Stage Lightweight Cryptography in IoT Cloud Systems |
    | CV | Computer Vision and Pattern Recognition | MetaSSL: A General Heterogeneous Loss for Semi-Supervised Medical Image Segmentation |
    | CY | Computers and Society | Understanding Fanchuan in Livestreaming Platforms: A New Form of Online Antisocial Behavior |
    | DB | Databases | Enabling Down Syndrome Research through a Knowledge Graph-Driven Analytical Framework |
    | DC | Distributed, Parallel, and Cluster Computing | LobRA: Multi-tenant Fine-tuning over Heterogeneous Data |
    | DL | Digital Libraries | How much are LLMs changing the language of academic papers after ChatGPT? A multi-database and full text analysis |
    | DM | Discrete Mathematics | CAZAC sequence generation of any length with iterative projection onto unit circle: principle and first results |
    | DS | Data Structures and Algorithms | The Steiner Shortest Path Tree Problem |
    | ET | Emerging Technologies | FCT O-RAN: Design and Deployment of a Multi-Vendor End-to-End Private 5G Testbed |
    | FL | Formal Languages and Automata Theory | Computational Exploration of Finite Semigroupoids |
    | GL | General Literature | Connections between reinforcement learning with feedback,test-time scaling, and diffusion guidance: An anthology |
    | GR | Graphics | Unifi3D: A Study on 3D Representations for Generation and Reconstruction in a Common Framework |
    | GT | Computer Science and Game Theory | Quantum game models for interaction-aware decision-making in automated driving |
    | HC | Human-Computer Interaction | AttenTrack: Mobile User Attention Awareness Based on Context and External Distractions |
    | IR | Information Retrieval | Empowering Large Language Model for Sequential Recommendation via Multimodal Embeddings and Semantic IDs |
    | IT | Information Theory | MUSE-FM: Multi-task Environment-aware Foundation Model for Wireless Communications |
    | LG | Machine Learning | ProCause: Generating Counterfactual Outcomes to Evaluate Prescriptive Process Monitoring Methods |
    | LO | Logic in Computer Science | An Information-Flow Perspective on Explainability Requirements: Specification and Verification |
    | MA | Multiagent Systems | Adaptive Evolutionary Framework for Safe, Efficient, and Cooperative Autonomous Vehicle Interactions |
    | MM | Multimedia | LLM-Guided Semantic Relational Reasoning for Multimodal Intent Recognition |
    | MS | Mathematical Software | DEViaN-LM: An R Package for Detecting Abnormal Values in the Gaussian Linear Model |
    | NA | Numerical Analysis | Learning functions through Diffusion Maps |
    | NE | Neural and Evolutionary Computing | Robustness and Invariance of Hybrid Metaheuristics under Objective Function Transformations |
    | NI | Networking and Internet Architecture | Green Traffic Engineering for Satellite Networks Using Segment Routing Flexible Algorithm |
    | OH | Other Computer Science | Modelling Scenarios for Carbon-aware Geographic Load Shifting of Compute Workloads |
    | OS | Operating Systems | Exploring Busy Period for Worst-Case Deadline Failure Probability Analysis |
    | PF | Performance | Optimal Parallel Scheduling under Concave Speedup Functions |
    | PL | Programming Languages | Dato: A Task-Based Programming Model for Dataflow Accelerators |
    | RO | Robotics | CARIS: A Context-Adaptable Robot Interface System for Personalized and Scalable Human-Robot Interaction |
    | SC | Symbolic Computation | An Effective Trajectory Planning and an Optimized Path Planning for a 6-Degree-of-Freedom Robot Manipulator |
    | SD | Sound | Music Genre Classification Using Machine Learning Techniques |
    | SE | Software Engineering | Automated Generation of Issue-Reproducing Tests by Combining LLMs and Search-Based Testing |
    | SI | Social and Information Networks | Towards Propagation-aware Representation Learning for Supervised Social Media Graph Analytics |
    | SY | Systems and Control | Improved PLL Design for Transient Stability Enhancement of Grid Following Converters Based on Lyapunov Method | 
  - 不同的数量：每批10个/20个/30个，多批次每个模型共生成120篇参考文献，也就是12次/6次/4次对话。每次开一个新的对话。
  - 使用不同的大模型：
    - 国外主流模型：GPT-5/Claude4/Gemini-2.5-Pro/Grok-4/Llama4
    - 国内主流模型：Qwen3/Doubao/Deepseek/GLM-4.5/kimi/文心一言
  - 表格填写要求：json格式，把每次对话的回复填在表格里

```
