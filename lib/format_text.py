from lib.docx_deserialization import QuestionBlock

def get_formatted_text(question_block: QuestionBlock) -> str:
    formatted_text = f"{question_block.question}\n{{\n"
    for i, answer in enumerate(question_block.answers):
        prefix = "= " if i == question_block.correct_answer else "~ "
        formatted_text += f"{prefix}{answer}\n"
    formatted_text += "}\n\n"
    return formatted_text