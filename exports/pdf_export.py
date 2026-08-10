from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
import os


def export_pdf(results):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{results['target']}_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph(
        "<b><font size=22 color='green'>ReconHub Scan Report</font></b>",
        styles["Title"]
    )

    story.append(title)

    story.append(Spacer(1,20))

    story.append(
        Paragraph(f"<b>Target:</b> {results['target']}", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Target Type:</b> {results['target_type']}", styles["BodyText"])
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph("<b>Modules Executed</b>", styles["Heading2"])
    )

    for module in results["modules"]:
        story.append(
            Paragraph(f"• {module}", styles["BodyText"])
        )

    story.append(Spacer(1,20))

    if "whois" in results:

        story.append(
            Paragraph("<b>WHOIS Information</b>", styles["Heading2"])
        )

        whois = results["whois"]

        for key, value in whois.items():

            story.append(
                Paragraph(f"<b>{key}</b>: {value}", styles["BodyText"])
            )

    if "dns" in results:

        story.append(Spacer(1,20))

        story.append(
            Paragraph("<b>DNS Records</b>", styles["Heading2"])
        )

        for record_type, values in results["dns"].items():

            story.append(
                Paragraph(f"<b>{record_type}</b>", styles["BodyText"])
            )

            if isinstance(values, list):

                for value in values:

                    story.append(
                        Paragraph(value, styles["BodyText"])
                    )

    if "subdomains" in results:

        story.append(Spacer(1,20))

        story.append(
            Paragraph("<b>Subdomains</b>", styles["Heading2"])
        )

        for sub in results["subdomains"]:

            story.append(
                Paragraph(sub, styles["BodyText"])
            )

    if results.get("technologies"):

        story.append(
        Paragraph("<b>Technology Fingerprinting</b>", styles["Heading2"])
    )

    for category, tech in results["technologies"]:

        story.append(
            Paragraph(
                f"<b>{category}</b>: {tech}",
                styles["BodyText"]
            )
        )

    if "ports" in results:

        story.append(Spacer(1,20))

        story.append(
            Paragraph("<b>Open Ports</b>", styles["Heading2"])
        )

        for port in results["ports"]:

            story.append(
                Paragraph(
                    f"{port['port']} ({port['service']})",
                    styles["BodyText"]
                )
            )

    doc.build(story)

    return filename