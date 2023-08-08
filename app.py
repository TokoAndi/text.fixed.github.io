from flask import Flask, render_template, request, Markup

app = Flask(__name__)


# Pindahkan kode pembacaan "kbbi.txt" ke sini
with open("kbbi.txt") as f:
    words = f.read().splitlines()


def find_matches(s):
    matches = []
    for word in words:
        if len(word) >= 2 and len(word) <= len(s):
            if all(word.count(c) <= s.count(c) for c in set(word)):
                matches.append(word)
    return matches


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    error_message = ""

    if request.method == "POST":
        input_text = request.form["input_text"]

        # Validasi untuk mencegah input hanya berisi spasi
        if input_text.strip() == "":
            error_message = "Input tidak boleh hanya berisi spasi"
        else:
            matches = find_matches(input_text)
            if matches:
                result = Markup("<br>".join(matches))
            else:
                result = "Tidak ada hasil ditemukan"

    return render_template("index.html", result=result, error_message=error_message)


if __name__ == "__main__":
    app.run(debug=True)
