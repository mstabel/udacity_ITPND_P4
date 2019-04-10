import media
import fresh_tomatoes


interstellar = media.Movie("Interstellar",
                "A Story about time.",
                "http://t0.gstatic.com/images?q=tbn:ANd9GcQGvmA1SH31axn8y51SzwVzHPNDJm2V4Xjvf8jTm1SqNOAwdnqF",
                "https://www.youtube.com/watch?v=zSWdZVtXT7E")
la_la_land = media.Movie("La La Land",
                "A story about a couple and two dreams.",
                "https://image.dhgate.com/0x0/f2/albu/g3/M00/C1/B1/rBVaHVn_N_WAAYSrAACZ5zLsiqk321.jpg",
                "https://www.youtube.com/watch?v=1bynVcygySE")
inception = media.Movie("Inception",
                "A story about reality and imagination",
                "https://images-na.ssl-images-amazon.com/images/I/91aB45kLV1L._SY445_.jpg",
                "https://www.youtube.com/watch?v=d3A3-zSOBT4")
the_intouchables = media.Movie("The Intouchables",
                    "A story about true friendship!",
                    "https://images-na.ssl-images-amazon.com/images/I/51po9WM6HKL._SY355_.jpg",
                    "https://www.youtube.com/watch?v=0RqDiYnFxTk")
atomic_blonde = media.Movie("Atomic Blonde",
                    "A story of agents during the cold war in berlin.",
                    "https://images-na.ssl-images-amazon.com/images/I/81y30g0lBKL._SY445_.jpg",
                    "https://www.youtube.com/watch?v=dVtqs38gr_I")
dunkirk = media.Movie("Dunkirk",
                "A story about the brutal WWII, taking place in Dunkirk.",
                "http://t3.gstatic.com/images?q=tbn:ANd9GcR3m-347Kzp7XbPAsnVQy8uAVq3xqUjdduXUsoWxob-i3Q7o1jh",
                "https://www.youtube.com/watch?v=F-eMt3SrfFU")

movies=[interstellar,la_la_land,inception,the_intouchables,atomic_blonde,dunkirk]
fresh_tomatoes.open_movies_page(movies)
