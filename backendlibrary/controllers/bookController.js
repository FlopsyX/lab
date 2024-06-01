const Book = require('../models/bookModel');
const multer = require('multer');

const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, 'uploads/');
    },
    filename: function (req, file, cb) {
        cb(null, Date.now() + '-' + file.originalname);
    }
});
const upload = multer({ storage: storage });

// Получить все книги
exports.getAllBooks = async (req, res) => {
    try {
        const books = await Book.find();
        res.status(200).json(books);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// Получить одну книгу
exports.getBook = async (req, res) => {
    try {
        const book = await Book.findById(req.params.id);
        if (!book) {
            return res.status(404).json({ message: 'Book not found' });
        }
        res.status(200).json(book);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// Создать книгу
exports.createBook = [
    upload.single('image'),
    async (req, res) => {
        console.log('Request body:', req.body); // Логируем тело запроса
        console.log('Uploaded file:', req.file); // Логируем файл
        const { title, author, description, download_url } = req.body;
        let image_url = req.file ? req.file.path : '';
        image_url = image_url.replace(/\\/g, '/');

        if (!title || !author || !description || !download_url) {
            return res.status(400).json({ message: 'All fields are required' });
        }

        const newBook = new Book({ title, author, description, download_url, image_url });

        try {
            await newBook.save();
            res.status(201).json(newBook);
        } catch (error) {
            res.status(400).json({ message: error.message });
        }
    }
];


// Обновить книгу
exports.updateBook = async (req, res) => {
    try {
        const book = await Book.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!book) {
            return res.status(404).json({ message: 'Book not found' });
        }
        res.status(200).json(book);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
};

// Удалить книгу
exports.deleteBook = async (req, res) => {
    try {
        const book = await Book.findByIdAndDelete(req.params.id);
        if (!book) {
            return res.status(404).json({ message: 'Book not found' });
        }
        res.status(200).json({ message: 'Book deleted' });
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};
