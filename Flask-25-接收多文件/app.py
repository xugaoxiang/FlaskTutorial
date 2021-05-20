from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def index():
    image_files = request.files.getlist('image')
    video_files = request.files.getlist('video')

    if not image_files and not video_files:
        return jsonify({
            "code": -1,
            "message": "No upload images or videos."
        })

    for image_file in image_files:
        image_file.save(image_file.filename)

    for video_file in video_files:
        video_file.save(video_file.filename)

    return jsonify({
        "code": 0,
        "message": "upload images and videos success."
    })


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=5000)
