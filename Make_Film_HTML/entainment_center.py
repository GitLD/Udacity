import media
import fresh_tomatoes

Annabelle_Comes_Home = media.Movie(
	'Annabelle Comes Home',
	'While babysitting the daughter of Ed and Lorraine Warren, a teenager and her friend unknowingly awaken an evil spirit trapped in a doll.',
	'https://m.media-amazon.com/images/M/MV5BYmI4NDNiMmQtZTFkYi00ZDVmLThlYTAtMWJlMjU1M2I2ZmViXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
	'https://www.imdb.com/video/imdb/vi1272953881?playlistId=tt8350360&ref_=tt_ov_vi'
	)

Avengers_Endgame = media.Movie(
	'Avengers:Endgame',
	"After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.",
	'https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',
	'https://www.imdb.com/video/imdb/vi2163260441?playlistId=tt4154796&ref_=tt_ov_vi'
	)

Men_in_Black = media.Movie(
	'Men in Black: International',
	"The Men in Black have always protected the Earth from the scum of the universe. In this new adventure, they tackle their biggest threat to date: a mole in the Men in Black organization.",
	'https://m.media-amazon.com/images/M/MV5BMDZkODI2ZGItYTY5Yi00MTA4LWExY2ItM2ZmNjczYjM0NDg1XkEyXkFqcGdeQXVyMzY0MTE3NzU@._V1_UX182_CR0,0,182,268_AL_.jpg',
	'https://www.imdb.com/video/imdb/vi1150073881?playlistId=tt2283336&ref_=tt_ov_vi'
	)

movie_list = [Annabelle_Comes_Home, Avengers_Endgame, Men_in_Black]
fresh_tomatoes.open_movies_page(movie_list)

