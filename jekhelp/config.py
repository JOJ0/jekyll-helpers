import confuse
import pprint

template = {
    'site_root': confuse.Path(),
    'images_dir': confuse.Path(relative_to='site_root'),
    'posts_dir': confuse.Path(relative_to='site_root'),
}

conf = confuse.Configuration('jekhelp', 'jekhelp')
valid_conf = conf.get(template)

root_dir = conf['site_root'].get()
images_dir = conf['images_dir'].get()
posts_dir = conf['posts_dir'].get()

print(valid_conf.posts_dir)
print(valid_conf.images_dir)
