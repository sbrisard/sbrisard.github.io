import datetime
import glob
import os.path
import re

def find_title(lines):
    p = re.compile(r'#\+TITLE:\s*(.*)')
    for line in lines:
        m = p.match(line)
        if m is not None:
            return m.group(1)
    return None

def find_date(lines):
    p = re.compile(r'#\+DATE:\s*<(20[0-9][0-9])-([0-9][0-9])-([0-9][0-9])')
    for line in lines:
        m = p.match(line)
        if m is not None:
            return datetime.date(*map(int, m.group(1, 2, 3)))
    return None

def find_abstract(lines):
    p1 = re.compile(r'#\+BEGIN_ABSTRACT')
    p2 = re.compile(r'#\+END_ABSTRACT')
    out = []
    m1 = None
    for line in lines:
        if m1 is None:
            m1 = p1.match(line)
        else:
            m2 = p2.match(line)
            if m2 is None:
                out.append(line)
            else:
                return out
    return out

def write_archives(name, path_to_posts, posts):
    with open(name, 'w', encoding='utf-8') as f:
        f.write('# -*- coding: utf-8; -*-\n')
        f.write('#+TITLE: Blog archive\n\n')
        for date, basename, title, abstract in posts:
            f.write('  - [[file:{0}][{1} -- {2}]]\n'.
                    format(path_to_posts + '/' + basename, date, title))

def write_home(name, path_to_posts, posts):
    with open(name, 'w', encoding='utf-8') as f:
        f.write('# -*- coding: utf-8; -*-\n')
        f.write('#+SETUPFILE: "./include/mathjax.org"\n')
        f.write('#+TITLE: Welcome!\n\n')
        f.write("You've reached the personal homepage of Sébastien Brisard. Please follow the links below.\n\n")
        for date, basename, title, abstract in posts[0:5]:
            f.write('* [[file:{0}][{1} -- {2}]]\n\n'.
                    format(path_to_posts + '/' + basename, date, title))
            for i in abstract:
                f.write(i + '\n')

if __name__ == '__main__':
    path_to_posts = os.path.join('..', 'org', 'posts')
    posts = list()
    for name in glob.iglob(os.path.join(path_to_posts, '*.org')):
        with open(name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            date = find_date(lines)
            title = find_title(lines)
            abstract = find_abstract(lines)
            if date is not None:
                posts.append((date, os.path.basename(name), title, abstract))

    posts.sort(reverse=True)

    write_archives(os.path.join('..', 'org', 'posts', 'archives.org'),
                   '.', posts)

    write_home(os.path.join('..', 'org', 'index.org'),
                   './posts', posts)
