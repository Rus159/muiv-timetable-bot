from html2image import HtmlToImage
import time
import os


def remove_pictures():
    folder = 'pictures/'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
            os.unlink(file_path)


def get_picture(data):
    remove_pictures()
    pixel_count = 8
    css_string = 'table {width: 100%; border-collapse: collapse;}\
        table td {padding: 12px 16px;}\
        table thead tr {font-weight: bold; border-top: 1px solid #e8e9eb;}\
        table tr {border-bottom: 1px solid #e8e9eb;}\
        table tbody tr:hover {background: #e8f6ff;}\
        html {background: #fff}'
    html_string = '<!DOCTYPE html>\n' + '<link rel="stylesheet" href="css.css">\n'+ '<html>\n' + '<table>\n'

    for day in data:
        html_string += '<tr>\n<th>' + day.capitalize() + '</th>\n'
        pixel_count += 21
        for lesson in data[day].items():
            html_string += '<tr><td>' + lesson[0] + '</td>\n' +\
                '<td>'+lesson[1][1] + '</td>' +\
                '<td>'+lesson[1][0] + '</td></tr>\n'
            pixel_count += 79
    html_string += '</table>\n' + '</html>'
    hti = HtmlToImage()
    hti.load_str(css_string, as_filename='css.css')
    hti.load_str(html_string, as_filename='timetable.html')
    hti.output_path = 'pictures/'
    pic_name = str(time.time()).replace('.', '') + '.png'
    hti.screenshot('timetable.html', pic_name, size=(600, pixel_count))
    file = open('pictures/' + pic_name, 'rb')
    return file
