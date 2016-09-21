const gulp = require('gulp');
const uglify = require('gulp-uglify');
const rename = require("gulp-rename");

gulp.task('mini', () => (
  ['app.js', 'controller.js', 'helpers.js', 'model.js', 'store.js', 'template.js', 'view.js'].forEach(file => {
    gulp.src('app/static/js/' + file)
    .pipe(uglify())    //uglify
    .pipe(gulp.dest('app/static/js/dist/'))
  })
));