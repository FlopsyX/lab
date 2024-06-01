const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const path = require('path')
const cors = require('cors');
const bookRoutes = require('./routes/bookRoutes');

dotenv.config();

const app = express();
app.use(cors({origin: "*"}));
const port = process.env.PORT || 8080;

app.use(express.json());
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

mongoose.connect(process.env.MONGO_URI).then(() => {
    console.log('Connected to MongoDB');
}).catch((error) => {
    console.error('Error connecting to MongoDB', error);
});

app.use('/api/books', bookRoutes);

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
