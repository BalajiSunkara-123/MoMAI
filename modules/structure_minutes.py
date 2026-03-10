def structure_minutes(summary):

    sentences = summary.split(".")
    
    filtered = []

    for s in sentences:
        s = s.strip()

        if len(s) < 25:
            continue

        if "is talking about" in s.lower():
            continue

        if "i have to check" in s.lower():
            continue

        filtered.append(s)

    context = filtered[0] if filtered else ""

    minutes = "\nMEETING MINUTES\n"
    minutes += "-------------------------\n\n"

    if context:
        minutes += "Meeting Context:\n"
        minutes += context + "\n\n"

    minutes += "Key Discussion Points:\n"
    for s in filtered[1:6]:
        minutes += f"• {s}\n"

    return minutes