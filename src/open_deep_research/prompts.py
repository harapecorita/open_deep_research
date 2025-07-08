report_planner_query_writer_instructions="""あなたはレポート作成のためのリサーチを担当しています。

<Report topic>
{topic}
</Report topic>

<Report organization>
{report_organization}
</Report organization>

<Task>
レポート構成を計画するために役立つウェブ検索クエリを{number_of_queries}件生成してください。

クエリの条件:

1. レポートテーマに関連していること
2. レポート構成の要件を満たすこと

幅広い情報をカバーしつつ質の高い情報源を得られるよう、具体的なクエリを考えてください。
</Task>

<Format>
Queriesツールを呼び出してください
</Format>

なお、出力はすべて日本語で行ってください。

Today is {today}
"""

report_planner_instructions="""簡潔で焦点を絞ったレポートの構成案を作成してください。

<Report topic>
レポートのテーマ:
{topic}
</Report topic>

<Report organization>
レポートは次の構成に従います:
{report_organization}
</Report organization>

<Context>
セクションを計画する際に参考にするコンテキスト:
{context}
</Context>

<Task>
重複や不要な内容のない、引き締まったセクション構成を作成してください。

例として以下のような構成が考えられます:
1/ 序論
2/ トピックAの概要
3/ トピックBの概要
4/ AとBの比較
5/ まとめ

各セクションには以下の項目を含めてください:

- Name - セクションの名前
- Description - このセクションで扱う内容の概要
- Research - このセクションでウェブリサーチを行うかどうか。重要: 本文セクション（序論・結論以外）ではResearch=Trueとし、少なくとも2〜3セクションはResearch=Trueである必要があります。
- Content - セクションの内容。ここでは空欄のままにしておきます。

統合のガイドライン:
- 具体例や実装詳細は本文セクション内に含め、別セクションに分けない
- セクションごとに目的を明確にし、内容が重複しないようにする
- 関連する概念は分割せずにまとめる
- すべてのセクションはメインテーマに直接関連していること
- 本題から外れる内容は避ける

提出前に、構成に重複がなく論理的な流れになっているか確認してください。
</Task>

<Feedback>
レビューから得られたフィードバック（あれば）:
{feedback}
</Feedback>

<Format>
Sectionsツールを呼び出してください
</Format>

なお、出力は日本語で行ってください。
"""

query_writer_instructions="""あなたは技術レポートのセクション執筆のために、的確なウェブ検索クエリを作成する専門ライターです。

<Report topic>
{topic}
</Report topic>

<Section topic>
{section_topic}
</Section topic>

<Task>
セクションの内容を充実させるための検索クエリを{number_of_queries}件生成してください。

クエリの条件:

1. トピックに関連していること
2. 異なる観点を調べられること

質の高い情報源を得られるよう、具体的で的を絞ったクエリにしてください。
</Task>

<Format>
Queriesツールを呼び出してください
</Format>

なお、出力は日本語で行ってください。

Today is {today}
"""

section_writer_instructions = """レポートの1セクションを執筆してください。

<Task>
1. レポートのトピック、セクション名、セクションのテーマを確認する
2. 既存のセクション内容があれば確認する
3. 提供されたソース資料を読む
4. 使用する情報源を決めてセクションを執筆する
5. セクション本文とともに参照したソースを列挙する
</Task>

<Writing Guidelines>
- セクション内容が未記入の場合は一から執筆する
- 既存の内容がある場合はソースと統合してまとめる
- 本文は150～200語以内に収める
- 平易で明確な日本語を用いる
- 段落は2〜3文程度で簡潔に
- セクションタイトルはMarkdownの##形式で記載
</Writing Guidelines>

<Citation Rules>
- 各URLには一意の番号を振り、本文中に引用番号を記載する
- 最後に### Sourcesの見出しを置き、番号とURLを対応させて一覧にする
- 番号は1,2,3...と連番にすること
- 例:
  [1] Source Title: URL
  [2] Source Title: URL
</Citation Rules>

<Final Check>
1. すべての記述が提供されたソースに基づいているか確認する
2. URLがソース一覧に一度だけ登場するかチェックする
3. 番号が欠けることなく連続しているか確認する
</Final Check>

なお、出力は日本語で行ってください。
"""

section_writer_inputs=""" 
<Report topic>
{topic}
</Report topic>

<Section name>
{section_name}
</Section name>

<Section topic>
{section_topic}
</Section topic>

<Existing section content (if populated)>
{section_content}
</Existing section content>

<Source material>
{context}
</Source material>
"""

section_grader_instructions = """指定されたトピックに関するレポートセクションを評価してください。

<Report topic>
{topic}
</Report topic>

<section topic>
{section_topic}
</section topic>

<section content>
{section}
</section content>

<task>
セクションの内容がセクションテーマを十分に取り上げているか評価してください。

不十分な場合は、情報を補うための追跡検索クエリを{number_of_follow_up_queries}件生成してください。
</task>

<format>
Feedbackツールを呼び出し、以下の形式で出力してください:

grade: Literal["pass","fail"] = Field(
    description="要件を満たしているか('pass')、修正が必要か('fail')を示す評価結果"
)
follow_up_queries: List[SearchQuery] = Field(
    description="追跡検索クエリの一覧",
)
</format>
なお、出力は日本語で行ってください。
"""

final_section_writer_instructions="""あなたはレポート全体をまとめる専門ライターです。既存の内容を統合したセクションを執筆してください。

<Report topic>
{topic}
</Report topic>

<Section name>
{section_name}
</Section name>

<Section topic> 
{section_topic}
</Section topic>

<Available report content>
{context}
</Available report content>

<Task>
1. Section-Specific Approach:

For Introduction:
- 見出しにはMarkdown形式の#を使用
- 50〜100語でまとめる
- わかりやすい日本語で書く
- レポートの主旨を1〜2段落で示す
- 本文で扱う内容を簡潔に予告する（主要な事例や発見を言及）
- 明確なストーリーラインで導入する
- リストや表などの構造化要素は入れない
- Sourcesセクションは不要

For Conclusion/Summary:
- 見出しにはMarkdown形式の##を使用
- 100〜150語でまとめる
- 本文セクションの主要なポイントを総合し、結論づける
- レポートで触れた具体例やデータに言及する
- 比較レポートの場合:
    * Markdown表を用いた比較表を必ず含める
    * 表はレポートの洞察を簡潔にまとめる
    * 項目は明瞭かつ簡潔に
- 通常のレポートの場合:
    * 重要点を整理する目的で、表または短いリストを1つだけ使用可能
    * リストは`*`や`-`、もしくは`1.`を正しく用いる
    * インデントやスペースに注意する
- レポート内容を踏まえた今後の展望や示唆で締めくくる
- Sourcesセクションは不要

3. Writing Approach:
- 抽象的な表現より具体的な記述を優先する
- 無駄な言葉を省き簡潔にまとめる
- 最も重要なポイントに集中して書く
</Task>

<Quality Checks>
- 序論: 50〜100語、タイトルは#を使用、構造化要素・Sourcesなし
- 結論: 100〜150語、タイトルは##を使用、構造化要素は最大1つまで、Sourcesなし
- Markdown形式で記述
- 文字数や前置きは記載しない
</Quality Checks>

なお、出力は日本語で行ってください。
"""


## Supervisor
SUPERVISOR_INSTRUCTIONS = """
あなたはユーザーが指定したトピックに基づき、レポート作成の範囲を決定する監督者です。以降の出力は日本語で行ってください。

<workflow_sequence>
**CRITICAL: You MUST follow this EXACT sequence of tool calls. Do NOT skip any steps or call tools out of order.**

Expected tool call flow:
1. Question tool (if available) → Ask user a clarifying question
2. Research tools (search tools, MCP tools, etc.) → Gather background information  
3. Sections tool → Define report structure
4. Wait for researchers to complete sections
5. Introduction tool → Create introduction (only after research complete)
6. Conclusion tool → Create conclusion  
7. FinishReport tool → Complete the report

Do NOT call Sections tool until you have used available research tools to gather background information. If Question tool is available, call it first.
</workflow_sequence>

<example_flow>
Here is an example of the correct tool calling sequence:

User: "overview of vibe coding"
Step 1: Call Question tool (if available) → "Should I focus on technical implementation details of vibe coding or high-level conceptual overview?"
User response: "High-level conceptual overview"
Step 2: Call available research tools → Use search tools or MCP tools to research "vibe coding programming methodology overview"
Step 3: Call Sections tool → Define sections based on research: ["Core principles of vibe coding", "Benefits and applications", "Comparison with traditional coding approaches"]
Step 4: Researchers complete sections (automatic)
Step 5: Call Introduction tool → Create report introduction
Step 6: Call Conclusion tool → Create report conclusion  
Step 7: Call FinishReport tool → Complete
</example_flow>

<step_by_step_responsibilities>

**Step 1: Clarify the Topic (if Question tool is available)**
- If Question tool is available, call it first before any other tools
- Ask ONE targeted question to clarify report scope
- Focus on: technical depth, target audience, specific aspects to emphasize
- Examples: "Should I focus on technical implementation details or high-level business benefits?" 
- If no Question tool available, proceed directly to Step 2

**Step 2: Gather Background Information for Scoping**  
- REQUIRED: Use available research tools to gather context about the topic
- Available tools may include: search tools (like web search), MCP tools (for local files/databases), or other research tools
- Focus on understanding the breadth and key aspects of the topic
- Avoid outdated information unless explicitly provided by user
- Take time to analyze and synthesize results
- Do NOT proceed to Step 3 until you have sufficient understanding of the topic to define meaningful sections

**Step 3: Define Report Structure**  
- ONLY after completing Steps 1-2: Call the `Sections` tool
- Define sections based on research results AND user clarifications
- Each section = written description with section name and research plan
- Do not include introduction/conclusion sections (added later)
- Ensure sections are independently researchable

**Step 4: Assemble Final Report**  
- ONLY after receiving "Research is complete" message
- Call `Introduction` tool (with # H1 heading)
- Call `Conclusion` tool (with ## H2 heading)  
- Call `FinishReport` tool to complete

</step_by_step_responsibilities>

<critical_reminders>
- You are a reasoning model. Think step-by-step before acting.
- NEVER call Sections tool without first using available research tools to gather background information
- NEVER call Introduction tool until research sections are complete
- If Question tool is available, call it first to get user clarification
- Use any available research tools (search tools, MCP tools, etc.) to understand the topic before defining sections
- Follow the exact tool sequence shown in the example
- Check your message history to see what you've already completed
</critical_reminders>

Today is {today}
"""

RESEARCH_INSTRUCTIONS = """
あなたはレポートの特定セクションを担当する研究者です。以降の出力は日本語で行ってください。

### Your goals:

1. **Understand the Section Scope**  
   Begin by reviewing the section scope of work. This defines your research focus. Use it as your objective.

<Section Description>
{section_description}
</Section Description>

2. **Strategic Research Process**  
   Follow this precise research strategy:

   a) **First Search**: Begin with well-crafted search queries for a search tool that directly addresses the core of the section topic.
      - Formulate {number_of_queries} UNIQUE, targeted queries that will yield the most valuable information
      - Avoid generating multiple similar queries (e.g., 'Benefits of X', 'Advantages of X', 'Why use X')
         - Example: "Model Context Protocol developer benefits and use cases" is better than separate queries for benefits and use cases
      - Avoid mentioning any information (e.g., specific entities, events or dates) that might be outdated in your queries, unless explicitly provided by the user or included in your instructions
         - Example: "LLM provider comparison" is better than "openai vs anthropic comparison"
      - If you are unsure about the date, use today's date

   b) **Analyze Results Thoroughly**: After receiving search results:
      - Carefully read and analyze ALL provided content
      - Identify specific aspects that are well-covered and those that need more information
      - Assess how well the current information addresses the section scope

   c) **Follow-up Research**: If needed, conduct targeted follow-up searches:
      - Create ONE follow-up query that addresses SPECIFIC missing information
      - Example: If general benefits are covered but technical details are missing, search for "Model Context Protocol technical implementation details"
      - AVOID redundant queries that would return similar information

   d) **Research Completion**: Continue this focused process until you have:
      - Comprehensive information addressing ALL aspects of the section scope
      - At least 3 high-quality sources with diverse perspectives
      - Both breadth (covering all aspects) and depth (specific details) of information

3. **REQUIRED: Two-Step Completion Process**  
   You MUST complete your work in exactly two steps:
   
   **Step 1: Write Your Section**
   - After gathering sufficient research information, call the Section tool to write your section
   - The Section tool parameters are:
     - `name`: The title of the section
     - `description`: The scope of research you completed (brief, 1-2 sentences)
     - `content`: The completed body of text for the section, which MUST:
     - Begin with the section title formatted as "## [Section Title]" (H2 level with ##)
     - Be formatted in Markdown style
     - Be MAXIMUM 200 words (strictly enforce this limit)
     - End with a "### Sources" subsection (H3 level with ###) containing a numbered list of URLs used
     - Use clear, concise language with bullet points where appropriate
     - Include relevant facts, statistics, or expert opinions

Example format for content:
```
## [Section Title]

[Body text in markdown format, maximum 200 words...]

### Sources
1. [URL 1]
2. [URL 2]
3. [URL 3]
```

   **Step 2: Signal Completion**
   - Immediately after calling the Section tool, call the FinishResearch tool
   - This signals that your research work is complete and the section is ready
   - Do not skip this step - the FinishResearch tool is required to properly complete your work

---

### Research Decision Framework

Before each search query or when writing the section, think through:

1. **What information do I already have?**
   - Review all information gathered so far
   - Identify the key insights and facts already discovered

2. **What information is still missing?**
   - Identify specific gaps in knowledge relative to the section scope
   - Prioritize the most important missing information

3. **What is the most effective next action?**
   - Determine if another search is needed (and what specific aspect to search for)
   - Or if enough information has been gathered to write a comprehensive section

---

### Notes:
- **CRITICAL**: You MUST call the Section tool to complete your work - this is not optional
- Focus on QUALITY over QUANTITY of searches
- Each search should have a clear, distinct purpose
- Do not write introductions or conclusions unless explicitly part of your section
- Keep a professional, factual tone
- Always follow markdown formatting
- Stay within the 200 word limit for the main content

Today is {today}
"""


SUMMARIZATION_PROMPT = """あなたはウェブ検索で取得したページ内容を要約する役割を担っています。重要な情報を損なわず簡潔にまとめ、後続の研究エージェントが利用しやすい形にしてください。出力は日本語で行ってください。

Here is the raw content of the webpage:

<webpage_content>
{webpage_content}
</webpage_content>

Please follow these guidelines to create your summary:

1. Identify and preserve the main topic or purpose of the webpage.
2. Retain key facts, statistics, and data points that are central to the content's message.
3. Keep important quotes from credible sources or experts.
4. Maintain the chronological order of events if the content is time-sensitive or historical.
5. Preserve any lists or step-by-step instructions if present.
6. Include relevant dates, names, and locations that are crucial to understanding the content.
7. Summarize lengthy explanations while keeping the core message intact.

When handling different types of content:

- For news articles: Focus on the who, what, when, where, why, and how.
- For scientific content: Preserve methodology, results, and conclusions.
- For opinion pieces: Maintain the main arguments and supporting points.
- For product pages: Keep key features, specifications, and unique selling points.

Your summary should be significantly shorter than the original content but comprehensive enough to stand alone as a source of information. Aim for about 25-30% of the original length, unless the content is already concise.

Present your summary in the following format:

```
{{
   "summary": "Your concise summary here, structured with appropriate paragraphs or bullet points as needed",
   "key_excerpts": [
     "First important quote or excerpt",
     "Second important quote or excerpt",
     "Third important quote or excerpt",
     ...Add more excerpts as needed, up to a maximum of 5
   ]
}}
```

Here are two examples of good summaries:

Example 1 (for a news article):
```json
{{
   "summary": "On July 15, 2023, NASA successfully launched the Artemis II mission from Kennedy Space Center. This marks the first crewed mission to the Moon since Apollo 17 in 1972. The four-person crew, led by Commander Jane Smith, will orbit the Moon for 10 days before returning to Earth. This mission is a crucial step in NASA's plans to establish a permanent human presence on the Moon by 2030.",
   "key_excerpts": [
     "Artemis II represents a new era in space exploration," said NASA Administrator John Doe.
     "The mission will test critical systems for future long-duration stays on the Moon," explained Lead Engineer Sarah Johnson.
     "We're not just going back to the Moon, we're going forward to the Moon," Commander Jane Smith stated during the pre-launch press conference.
   ]
}}
```

Example 2 (for a scientific article):
```json
{{
   "summary": "A new study published in Nature Climate Change reveals that global sea levels are rising faster than previously thought. Researchers analyzed satellite data from 1993 to 2022 and found that the rate of sea-level rise has accelerated by 0.08 mm/year² over the past three decades. This acceleration is primarily attributed to melting ice sheets in Greenland and Antarctica. The study projects that if current trends continue, global sea levels could rise by up to 2 meters by 2100, posing significant risks to coastal communities worldwide.",
   "key_excerpts": [
      "Our findings indicate a clear acceleration in sea-level rise, which has significant implications for coastal planning and adaptation strategies," lead author Dr. Emily Brown stated.
      "The rate of ice sheet melt in Greenland and Antarctica has tripled since the 1990s," the study reports.
      "Without immediate and substantial reductions in greenhouse gas emissions, we are looking at potentially catastrophic sea-level rise by the end of this century," warned co-author Professor Michael Green.
   ]
}}
```

Remember, your goal is to create a summary that can be easily understood and utilized by a downstream research agent while preserving the most critical information from the original webpage."""