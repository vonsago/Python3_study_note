import fresh_tomatoes
import movie

mymovie1=movie.Movie("a Strange Story1","what the fuck1","https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1490010723160&di=c382774e164811c59355dcb5f9884ac9&imgtype=0&src=http%3A%2F%2Fpic36.photophoto.cn%2F20150707%2F0047045135399298_b.jpg","https://bing.com")

mymovie2=movie.Movie("a Strange Story2","what the fuck2","https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1490010762591&di=bc541e7c6a40ec66089be8fff16b2e37&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F32dcd52a6059252d627887f8349b033b5ab5b981.jpg","https://bing.com")

mymovie3=movie.Movie("a Strange Story3","what the fuck3","https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1490010764688&di=e41912c3aff7471c3b267b123d742152&imgtype=0&src=http%3A%2F%2Fpic.qiantucdn.com%2F58pic%2F21%2F44%2F25%2F30B58PIC8gH_1024.jpg","https://bing.com")

mymovie4=movie.Movie("a Strange Story4","what the fuck4","https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1490010781537&di=d65961d8fd76b0611bef8212471e6444&imgtype=0&src=http%3A%2F%2Fpic.qiantucdn.com%2F58pic%2F19%2F74%2F33%2F5710906c5b083_1024.jpg","https://bing.com")

movies = [mymovie1,mymovie2,mymovie3,mymovie4]

print(movie.Movie.__doc__)
print(movie.Movie.__name__)
print(movie.Movie.__module__)
#fresh_tomatoes.open_movies_page(movies)
