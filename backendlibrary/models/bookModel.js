const mongoose = require('mongoose');

const bookSchema = new mongoose.Schema({
    title: { type: String },
    author: { type: String },
    description: { type: String },
    download_url: { type: String },
    image_url: { type: String }, // добавлено поле для хранения пути к изображению
});

module.exports = mongoose.model('Book', bookSchema);
