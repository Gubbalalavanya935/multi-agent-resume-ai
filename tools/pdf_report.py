from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_report(result):

    file_path = "candidate_report.pdf"

    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("AI Resume Analysis Report", styles["Heading1"]))
    content.append(Spacer(1, 20))

    content.append(Paragraph("Resume Analysis", styles["Heading2"]))
    content.append(Paragraph(result["resume"], styles["BodyText"]))
    content.append(Spacer(1, 20))

    content.append(Paragraph("Job Requirements", styles["Heading2"]))
    content.append(Paragraph(result["job"], styles["BodyText"]))
    content.append(Spacer(1, 20))

    content.append(Paragraph("Match Result", styles["Heading2"]))
    content.append(Paragraph(result["match"], styles["BodyText"]))
    content.append(Spacer(1, 20))

    content.append(Paragraph("Final Decision", styles["Heading2"]))
    content.append(Paragraph(result["decision"], styles["BodyText"]))

    pdf = SimpleDocTemplate(file_path)

    pdf.build(content)

    return file_path