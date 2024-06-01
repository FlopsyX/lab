const express = require('express');
const router = express.Router();
const bookController = require('../controllers/bookController');

router.get('/', bookController.getAllBooks);
router.get('/:id', bookController.getBook);
router.post('/', bookController.createBook); // Используем upload.single для обработки одного файла
router.put('/:id', bookController.updateBook); // Используем upload.single для обработки одного файла
router.delete('/:id', bookController.deleteBook);

module.exports = router;
