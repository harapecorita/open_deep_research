clarify_with_user_instructions="""
以下は、ユーザーがレポートを要求した際にやり取りされたメッセージです。
<Messages>
{messages}
</Messages>

レポートの範囲を明確にするため、1つだけ質問を返してください。
着目すべき点: 技術的深さ、想定読者、強調すべき観点
例: "技術的な実装詳細に焦点を当てるべきですか、それともハイレベルなビジネスメリットにすべきですか?"
出力は日本語で行ってください。
"""

report_planner_query_writer_instructions="""あなたはレポート作成のためのリサーチを行います。

以下はレポートを依頼したユーザーとのこれまでのメッセージです。
<Messages>
{messages}
</Messages>

レポートは次の構成に従います:
<Report organization>
{report_organization}
</Report organization>

<Task>
レポートの各セクションを計画するためのウェブ検索クエリを{number_of_queries}件生成してください。

クエリの条件:

1. レポートのテーマに関連していること
2. レポート構成の要件を満たすこと

幅広い情報をカバーしつつ質の高い情報源を得られるよう、具体的なクエリにしてください。
</Task>

<Format>
Queriesツールを呼び出してください
</Format>

出力は日本語で行ってください。

Today is {today}
"""

report_planner_instructions="""簡潔で焦点を絞ったレポートの構成案を作成してください。

以下はユーザーからレポートを依頼された際のメッセージ履歴です。
<Messages>
{messages}
</Messages>

レポートは次の構成に従います:
<Report organization>
{report_organization}
</Report organization>

以下のコンテキストを参考にセクションを計画してください:
<Context>
{context}
</Context>

<Task>
重複や余計な内容を含まない引き締まったセクション構成を作成してください。

例として以下のような構成が考えられます:
1/ intro
2/ overview of topic A
3/ overview of topic B
4/ comparison between A and B
5/ conclusion

各セクションには次の項目を含めてください:

- Name - Name for this section of the report.
- Description - Brief overview of the main topics covered in this section.
- Research - Whether to perform web research for this section of the report. IMPORTANT: Main body sections (not intro/conclusion) MUST have Research=True. A report must have AT LEAST 2-3 sections with Research=True to be useful.
- Content - The content of the section, which you will leave blank for now.

統合のガイドライン:
- Include examples and implementation details within main topic sections, not as separate sections
- Ensure each section has a distinct purpose with no content overlap
- Combine related concepts rather than separating them
- CRITICAL: Every section MUST be directly relevant to the main topic
- Avoid tangential or loosely related sections that don't directly address the core topic

提出前に、構成に重複がなく論理的な流れになっているか確認してください。
</Task>

<Feedback>
レビューからのフィードバック（あれば）:
{feedback}
</Feedback>

<Format>
Sectionsツールを呼び出してください
</Format>

出力は日本語で行ってください。
"""

query_writer_instructions="""あなたは技術レポート執筆のための検索クエリを作成する専門ライターです。

以下はユーザーとのこれまでのメッセージです。
<Messages>
{messages}
</Messages>

<Section topic>
{section_topic}
</Section topic>

<Task>
セクションを充実させるための検索クエリを{number_of_queries}件生成してください。

クエリの条件:

1. トピックに関連していること
2. 異なる観点を調べられること

質の高い情報源を得られるよう、具体的なクエリにしてください。
</Task>

<Format>
Queriesツールを呼び出してください
</Format>

出力は日本語で行ってください。

Today is {today}
"""

section_writer_instructions = """レポートの1セクションを執筆してください。

<Task>
1. レポート依頼に関するメッセージ、セクション名、セクションのテーマを確認する
2. 既存のセクション内容があれば確認する
3. 提供されたソース資料を読む
4. 使用する情報源を決めてセクションを執筆する
5. セクション本文とともに参照したソースを列挙する
</Task>

<Writing Guidelines>
- セクション内容が未記入の場合は一から執筆する
- 既存の内容がある場合はソースと統合してまとめる
- 本文は150〜200語以内に収める
- 平易で明確な日本語を用いる
- 段落は2〜3文程度で簡潔に
- セクションタイトルはMarkdownの##形式で記載
- 自分が書いていることを示す表現は使わない
- 作業内容のコメントは入れない
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
4. 自分の作業についてのコメントは書かず、セクション本文のみを記載する
</Final Check>

なお、出力は日本語で行ってください。
"""

section_writer_inputs=""" 
These are the messages that have been exchanged so far from the user asking for the report:
<Messages>
{messages}
</Messages>

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

section_grader_instructions = """指定されたトピックに対するレポートセクションを評価してください。

以下はユーザーとのやり取りです。
<Messages>
{messages}
</Messages>

<section topic>
{section_topic}
</section topic>

<section content>
{section}
</section content>

<task>
セクションの内容がセクションテーマを十分に扱っているか評価してください。

不十分な場合は、情報補完のための追加検索クエリを{number_of_follow_up_queries}件生成してください。
</task>

<format>
Feedbackツールを呼び出し、次の形式で出力してください:

grade: Literal["pass","fail"] = Field(
    description="要件を満たしているか('pass')、修正が必要か('fail')を示す評価結果"
)
follow_up_queries: List[SearchQuery] = Field(
    description="追加検索クエリの一覧",
)
</format>
なお、出力は日本語で行ってください。
"""

final_section_writer_instructions="""あなたはレポート全体をまとめる専門ライターです。既存の情報を統合したセクションを執筆してください。

These are the messages that have been exchanged so far from the user asking for the report:
<Messages>
{messages}
</Messages>

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
- レポートの主旨を1〜2段落で述べる
- 本文で扱う内容を簡潔に予告する（主要な事例や発見を言及）
- 明確なストーリーで導入する
- リストや表などの構造化要素は入れない
- Sourcesセクションは不要

For Conclusion/Summary:
- 見出しにはMarkdown形式の##を使用
- 100〜150語でまとめる
- 本文セクションの要点を総合し結論づける
- レポートで触れた具体例やデータに触れる
- 比較レポートの場合:
    * Markdown表を用いた比較表を必ず含める
    * 表は洞察を簡潔にまとめる
    * 項目は明瞭かつ簡潔に
- 通常のレポートの場合:
    * 重要点を整理する目的で、表または短いリストを1つだけ使用可能
    * リストは`*`や`-`、`1.`を適切に使う
    * インデントやスペースに注意する
- レポート内容を踏まえた今後の展望や示唆で締めくくる
- Sourcesセクションは不要

3. Writing Approach:
- 抽象的な表現より具体的な記述を優先する
- 不要な言葉を省き簡潔にまとめる
- 最も重要なポイントに集中して書く
</Task>

<Quality Checks>
- 序論: 50〜100語、タイトルは#を使用、構造化要素・Sourcesなし
- 結論: 100〜150語、タイトルは##を使用、構造化要素は最大1つまで、Sourcesなし
- Markdown形式で記述
- 文字数や前置きは記載しない
- 自分を示す表現は使わない
</Quality Checks>

なお、出力は日本語で行ってください。
"""

SUMMARIZATION_PROMPT = """あなたはウェブ検索で取得したページの内容を要約する役割を担っています。重要な情報を損なわず簡潔にまとめ、後続の研究エージェントが利用しやすいようにしてください。出力は日本語で行ってください。

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