from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


def main():
    # MODEL
    model = OllamaLLM(model="gemma3:1b")

    # PROMPT
    template = """Question: {question}
    Answer: ステップバイステップで考えてみましょう。"""
    prompt = ChatPromptTemplate.from_template(template)

    # CHAIN
    chain = prompt | model
    result = chain.invoke({"question": "美味しいパスタの作り方は?"})
    print(result)


if __name__ == "__main__":
    main()
