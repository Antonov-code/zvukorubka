// var comments = new Vue({
//     delimiters: ["[[", "]]"],
//     el: '#comments',
//     data() {
//       return {
//         comments: [] // Массив для хранения полученных данных
//       };
//     },
//     mounted() {
//       fetch('/api/comments/')
//         .then(response => response.json()) // Преобразуем в JSON
//         .then(data => {
//           this.comments = data; // Сохраняем в переменную
//         })
//         .catch(error => console.error('Ошибка:', error));
//     },
//   })
