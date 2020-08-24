MDOT APP
========

This README documents whatever steps are necessary to get your application up and running.

## Use Docker ##

**Steps (make sure Docker & Docker Compose is installed)**

    $ git clone https://github.com/uw-it-aca/mdot.git

After cloning the project, you need to create a `local.py` file within the directory `mdot/sampleproj/settings`. There already is an example of what the `local.py` file should be. To get started, simply copy the `example-local.py` file and name it `local.py`

    $ cp example-local.py local.py

Return to the parent (`mdot`) directory and:

    $ docker-compose up

## Installing the application ##

**Create a virtualenv for your project**

    $ virutualenv yourenv
    $ cd yourenv
    $ source bin/activate

**Install Mdot app**  

    $ (yourenv) pip install -e git+https://github.com/uw-it-aca/mdot/#egg=mdot
    $ (yourenv) pip install -e git+https://github.com/uw-it-aca/mdot-developers/#egg=mdotdevs

**Create an empty Django project**

    $ (yourenv) django-admin.py startproject yourproj .
    $ (yourenv) cd yourproj

**Update your urls.py**

    urlpatterns = patterns('',
        ...
        url(r'^developers', include('mdotdevs.urls')),
        url(r'^', include('mdot.urls')),
    )

**Update your settings.py**

    INSTALLED_APPS = (
        ...
        'templatetag_handlebars',
        'easy_pjax',
        'mdot',
        'mdotdevs',
        'compressor',
    )

    MIDDLEWARE_CLASSES = (
        ...
        'django_mobileesp.middleware.UserAgentDetectionMiddleware',
        'htmlmin.middleware.HtmlMinifyMiddleware',
        'htmlmin.middleware.MarkRequestMiddleware',
    )

    TEMPLATES = [
        {
            ...
            'OPTIONS': {
                'context_processors': [
                    ...
                    'mdot.context_processors.less_compiled',
                    'mdot.context_processors.google_analytics',
                    'mdot.context_processors.devtools_bar',
                ]
            }
        }
    ]

    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
        'compressor.finders.CompressorFinder',
    )

    COMPRESS_ROOT = "/tmp/some/path/for/files"
    COMPRESS_PRECOMPILERS = (('text/less', 'lessc {infile} {outfile}'),)
    COMPRESS_ENABLED = False # True if you want to compress your development build
    COMPRESS_OFFLINE = False # True if you want to compress your build offline
    COMPRESS_CSS_FILTERS = [
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.CSSMinFilter'
    ]
    COMPRESS_JS_FILTERS = [
        'compressor.filters.jsmin.JSMinFilter',
    ]

    # devtools
    ACA_DEVTOOLS_ENABLED = True

    # mobileesp
    from django_mobileesp.detector import mobileesp_agent as agent

    DETECT_USER_AGENTS = {
        'is_android': agent.detectAndroid,
        'is_ios': agent.detectIos,
        'is_windows_phone': agent.detectWindowsPhone,
        'is_tablet' : agent.detectTierTablet,
        'is_mobile': agent.detectMobileQuick,
    }

    # htmlmin
    HTML_MINIFY = True

**Create your database**

    $ (yourenv) python manage.py syncdb

**Run your server:**

    $ (yourenv) python manage.py runserver 0:8000


**It worked!**

    You should see the Django server running when viewing http://localhost:8000
