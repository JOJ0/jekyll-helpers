import confuse
import pprint

template = {
    'site_root': confuse.Path(),
    'images_dir': confuse.Path(relative_to='site_root'),
    'posts_dir': confuse.Path(relative_to='site_root'),
}

conf = confuse.Configuration('jekhelp', 'jekhelp')
valid_conf = conf.get(template)
