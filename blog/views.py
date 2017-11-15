from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from blog.models import Blog_data
from blog.at_file_parse import *

from blog.models import Market_data
from blog.models import Board_data


# Create your views here.

# Board
board_url = 'http://plus.cnu.ac.kr/_prog/_board/?code=sub07_070801&site_dvs_cd=kr&menu_dvs_cd=070801'
# Market
market_url = 'http://plus.cnu.ac.kr/_prog/_board/?code=sub07_070802&site_dvs_cd=kr&menu_dvs_cd=070802'

def url_parse(url, index):
    req = requests.get(url)
    plain_text = req.content
    soup = BeautifulSoup(plain_text, 'lxml')
    posts = soup.select("td.title > a")[index]
    parser_url = 'http://plus.cnu.ac.kr/_prog/_board/' + posts.get('href')[2:]
    compare_test = posts.get_text() # 최신 제목`

    return parser_url, compare_test

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def blog_data(request):
    parser_data = Blog_data.objects.filter(text__contains="[인재개발원]")
    return render(request, 'blog/post_list.html', {'parser':parser_data})

def parse_data(request):
    parser_url, compare_test = url_parse(market_url, 1)
    title_path = os.path.abspath("title_check.txt")
    compare = parser(compare_test, title_path)
    if compare == True:
        src_parser(parser_url)
    market_data = Market_data.objects.all()
    return render(request, 'blog/market_list.html', {'market':market_data})

def board_data(request):
    parser_url, compare_test = url_parse(board_url, 0)
    title_path = os.path.abspath("title_check_board.txt")
    compare = parser(compare_test, title_path)
    if compare == True:
        src_parser(parser_url)
    board_data = Board_data.objects.all()
    return render(request, 'blog/board_list.html', {'board':board_data})
