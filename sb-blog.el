;; -*- coding: utf-8 -*-
(require 'dash)
(require 'f)
(require 'ox)
(require 's)

;; Global variables
;; ================

;; Get path to file being loaded.
(defvar sb-blog-root (file-name-directory load-file-name))
(defvar sb-blog-base-directory (concat sb-blog-root "org/"))
(defvar sb-blog-publishing-directory (concat sb-blog-root "html/"))
(defvar sb-blog-pages-base-directory (concat sb-blog-root "org/pages"))
(defvar sb-blog-pages-publishing-directory (concat sb-blog-root "html/pages"))
(defvar sb-blog-posts-base-directory (concat sb-blog-root "org/posts"))
(defvar sb-blog-posts-sitemap-filename "archives.org")
(defvar sb-blog-posts-publishing-directory (concat sb-blog-root "html/posts"))

;; Path manipulations
;; ==================

(defun sb-blog-path-to-root (level)
  (apply 'f-join "." (make-list level "..")))

(defun sb-blog-path-depth (path)
  (length (-filter (lambda (item) (not (equal item "."))) (f-split path))))

(defun sb-blog-get-level ()
  (sb-blog-path-depth (f-relative (file-name-directory buffer-file-name)
                                  sb-blog-base-directory)))

;; Scripts for embedded gadgets
;; ============================

;; Twitter buttons
;; ---------------
(defvar sb-blog-twitter-follow-button-script "<a href=\"https://twitter.com/SebBrisard\" class=\"twitter-follow-button\" data-show-count=\"false\">Follow @SebBrisard</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>
")

;; Disqus comments embed
;; ---------------------
(defvar sb-blog-disqus-script-format "<div id=\"disqus_thread\"></div>
<script type=\"text/javascript\">
var disqus_shortname = 'sbrisard';
var disqus_identifier = '%s';
var disqus_title = '%s';
var disqus_url = '%s';
(function() {
var dsq = document.createElement('script');
dsq.type = 'text/javascript';
dsq.async = true;
dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
})();
</script>
<noscript>Please enable JavaScript to view the <a href=\"http://disqus.com/?ref_noscript\">comments powered by Disqus.</a></noscript>
<a href=\"http://disqus.com\" class=\"dsq-brlink\">blog comments powered by <span class=\"logo-disqus\">Disqus</span></a>
")

(defun sb-blog-disqus-script (info)
  (let (id url)
    (setq id (s-chop-prefix sb-blog-base-directory
                            (s-chop-suffix ".org" buffer-file-name)))
    (setq url (concat "http://sbrisard.github.io/" id ".html"))
    (format sb-blog-disqus-script-format
            id
            (org-export-data (plist-get info :title) info)
            url)))

;; Functions for generation of HTML tags
;; =====================================

(defun sb-blog-fa (name)
  (format "<span class=\"fa fa-%s\"></span>" name))

(defun sb-blog-list-item (item)
  (concat "<li>" item "</li>\n"))

(defun sb-blog-unordered-list (items)
  (concat "<ul>\n" (mapconcat 'sb-blog-list-item items nil) "</ul>\n"))

(defun sb-blog-link (link title description)
  (format "<a href=\"%s\" title=\"%s\">%s</a>" link title description))

(defun sb-blog-rel-link (link title description level)
  (sb-blog-link (f-join (sb-blog-path-to-root level) link) title description))

(defun sb-blog-banner (level)
  (format "<img id=\"banner\" src=\"%s\"/>\n"
          (f-join (sb-blog-path-to-root level) "images" "banner.jpg")))

(defun sb-blog-link-home (level)
  (sb-blog-rel-link "index.html" "Home" (sb-blog-fa "home") level))

(defun sb-blog-link-about (level)
  (sb-blog-rel-link "pages/about.html" "About me" (sb-blog-fa "user") level))

(defun sb-blog-link-references (level)
  (sb-blog-rel-link "pages/references.html" "References" (sb-blog-fa "book")
                    level))

(defun sb-blog-link-archives (level)
  (sb-blog-rel-link "posts/archives.html" "Archives" (sb-blog-fa "archive")
                    level))

(defun sb-blog-link-rss (level)
  (sb-blog-rel-link "feed.xml" "RSS" (sb-blog-fa "rss") level))

(defvar sb-blog-link-twitter (sb-blog-link "https://twitter.com/SebBrisard"
                                           "Twitter"
                                           (sb-blog-fa "twitter")))

(defvar sb-blog-link-github (sb-blog-link "https://github.com/sbrisard"
                                          "GitHub"
                                          (sb-blog-fa "github")))

(defvar sb-blog-link-bitbucket (sb-blog-link "https://bitbucket.org/sbrisard"
                                             "Bitbucket"
                                             (sb-blog-fa "bitbucket")))


;; Custom backend
;; ==============

(org-export-define-derived-backend 'sb-blog 'html
                                   :export-block "SB BLOG"
                                   :options-alist
                                   '((:comments-allowed nil "comments" nil)))

(defun sb-blog-publish-to-html (plist filename pub-dir)
  (org-publish-org-to 'sb-blog filename
		      (concat "." (or (plist-get plist :html-extension)
				      org-html-extension "html"))
		      plist pub-dir))


(defun sb-blog-html-head (level)
  (concat (format "<link rel=\"stylesheet\" href=\"%s\"/>"
                  (f-join (sb-blog-path-to-root level) "theme.css"))
          "<link rel=\"stylesheet\" href=\"http://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css\">"))

(defun sb-blog-html-preamble (info)
  (let ((level (sb-blog-get-level)))
    (concat (sb-blog-banner level)
            "<div class=\"navbar\">\n"
            (sb-blog-unordered-list `(,(sb-blog-link-home level)
                                      ,(sb-blog-link-about level)
                                      ,(sb-blog-link-references level)
                                      ,(sb-blog-link-archives level)
                                      ,sb-blog-link-github
                                      ,sb-blog-link-bitbucket
                                      ,sb-blog-link-twitter
                                      ,(sb-blog-link-rss level)))
            "</div>\n")))

;; To allow for comments
;; #+OPTIONS: comments:t
(defun sb-blog-html-postamble (info)
  (concat "<p>This blog was generated with <a href=\"http://www.gnu.org/software/emacs/\">Emacs</a> and <a href=\"http://orgmode.org/\">Org mode</a>. The theme is inspired from <a href=\"http://orgmode.org/worg/\">Worg</a>. Icons come from the <a href=\"http://fontawesome.io/\">Font Awesome</a> icon set.</p>
"
          sb-blog-twitter-follow-button-script
          (when (and (plist-get info :comments-allowed)
                     (not (s-ends-with? sb-blog-posts-sitemap-filename
                                        buffer-file-name)))
            (sb-blog-disqus-script info))))

;; From http://lists.gnu.org/archive/html/emacs-orgmode/2008-11/msg00571.html
;;
;; Hi Richard,
;;
;; no, variables are not interpolated into quoted lists, any list preceded by
;; "'" is quoted.
;;
;; If you can guarantee that the value of the variables is defined at the time
;; the
;;
;;   (setq org-publish-projects-alist ...
;;
;; is executed, then you can use backquote syntax: Quote the main list with
;; the backquote, and then preceed any variable inside you would like to
;; have evaluated with a comma so
;;
;; (setq org-publish-projects-alist
;;        `( .............
;;            ,rgr-souerce
;;            ....))
;;
;; Note that this works only once, so if you later change the value, this list
;; will not be changed.
::
;; If you wanted dynamic behavior, then we would have to patch org-publish.el.
;;
;; HTH
;;
;; - Carsten
;;
(setq org-publish-project-alist
      `(("sb-blog-root"
         :base-directory ,sb-blog-base-directory
         :publishing-directory ,sb-blog-publishing-directory
         :base-extension "org"
         :exclude nil
         :recursive nil
         :publishing-function sb-blog-publish-to-html
         :auto-sitemap nil
         :html-doctype "html5"
         :html-container "div"
         :html-head ,(sb-blog-html-head 0)
         :html-head-include-default-style nil
         :html-head-include-scripts nil
         :html-preamble nil
         :html-preamble sb-blog-html-preamble
         :html-postamble sb-blog-html-postamble
         :section-numbers nil
         :with-toc nil
         :language "en"
         :comments-allowed nil
         )
        ("sb-blog-pages"
         :base-directory ,sb-blog-pages-base-directory
         :publishing-directory ,sb-blog-pages-publishing-directory
         :base-extension "org"
         :exclude nil
         :recursive t
         :publishing-function sb-blog-publish-to-html
         :auto-sitemap nil
         :sitemap-sort-files chronologically
         :html-doctype "html5"
         :html-container "div"
         :html-head ,(sb-blog-html-head 1)
         :html-head-include-default-style nil
         :html-head-include-scripts nil
         :html-preamble sb-blog-html-preamble
         :html-postamble sb-blog-html-postamble
         :section-numbers nil
         :with-toc nil
         :language "en"
         :comments-allowed nil
         )
        ("sb-blog-posts"
         :base-directory ,sb-blog-posts-base-directory
         :publishing-directory ,sb-blog-posts-publishing-directory
         :base-extension "org"
         :exclude nil
         :recursive t
         :publishing-function sb-blog-publish-to-html
         :auto-sitemap t
         :sitemap-filename ,sb-blog-posts-sitemap-filename
         :sitemap-title "Blog archive"
         :sitemap-sort-files anti-chronologically
         :sitemap-file-entry-format "%d -- %t"
         :html-doctype "html5"
         :html-container "div"
         :html-head ,(sb-blog-html-head 1)
         :html-head-include-default-style nil
         :html-head-include-scripts nil
         :html-preamble sb-blog-html-preamble
         :html-postamble sb-blog-html-postamble
         :section-numbers nil
         :with-toc nil
         :language "en"
         :comments-allowed t
         )
        ("sb-blog-attachments"
         :base-directory ,sb-blog-base-directory
         :publishing-directory ,sb-blog-publishing-directory
         :base-extension "jpg\\|gif\\|png\\|xml\\|css"
         :recursive t
         :publishing-function org-publish-attachment)
        ("sb-blog"
         :components ("sb-blog-root"
                      "sb-blog-pages"
                      "sb-blog-posts"
                      "sb-blog-attachments"))))
