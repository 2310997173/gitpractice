const path = require('path');
module.exports={
    mode: "production",
    entry: "./src/App.js",
    output:{
        path: path.resolve(__dirname,'dist'),
        filename: "main.js"
    },
    devServer:{
        static: {
            directory: path.join(__dirname,'dist'),
        },
        compress: true,
        port: 5500,
        hot: true
    }
}