;; -*- coding: utf-8 -*-
;; Get path to file being loaded.
(defvar sb-blog-root (file-name-directory load-file-name))
(defvar sb-blog-base-directory (concat sb-blog-root "org/"))
(defvar sb-blog-publishing-directory (concat sb-blog-root "html/"))
(defvar sb-blog-pages-base-directory (concat sb-blog-root "org/pages"))
(defvar sb-blog-pages-publishing-directory (concat sb-blog-root "html/pages"))
(defvar sb-blog-posts-base-directory (concat sb-blog-root "org/posts"))
(defvar sb-blog-posts-publishing-directory (concat sb-blog-root "html/posts"))
(defvar sb-blog-css-base-directory (concat sb-blog-root "css/"))
(defvar sb-blog-css-publishing-directory (concat sb-blog-publishing-directory
                                                 "css/"))

(defun sb-blog-path-to-root (level)
  (let ((path "./"))
    (dotimes (number level path)
      (setq path (concat path "../")))))

(defun sb-blog-link (link description)
  (format "<a href=\"%s\">%s</a>" link description))

(defun sb-blog-rel-link (link description level)
  (sb-blog-link (concat (sb-blog-path-to-root level) link) description))

(defun sb-blog-html-head (level)
  (format "<link href=\"%scss/theme.css\" rel=\"stylesheet\" />"
          (sb-blog-path-to-root level)))

(defvar sb-blog-html-head-extra "<script type=\"text/javascript\">window.twttr = (function (d, s, id) {var t, js, fjs = d.getElementsByTagName(s)[0]; if (d.getElementById(id)) return; js = d.createElement(s); js.id = id; js.src= \"https://platform.twitter.com/widgets.js\"; fjs.parentNode.insertBefore(js, fjs); return window.twttr || (t = { _e: [], ready: function (f) { t._e.push(f) } }); }(document, \"script\", \"twitter-wjs\"));</script>")

(defun sb-blog-html-preamble (level)
  (let ((sep "&nbsp;&nbsp;&nbsp;&nbsp;"))
    (concat "<div class=\"navbar\">"
            (sb-blog-rel-link "index.html" "Home" level)
            sep
            (sb-blog-rel-link "pages/about.html" "About me" level)
            sep
            (sb-blog-rel-link "pages/references.html" "References" level)
            sep
            (sb-blog-rel-link "posts/archives.html" "Archives" level)
            "</div")))

(defvar sb-blog-html-postamble "<a class=\"twitter-follow-button\" href=\"https://twitter.com/SebBrisard\" data-show-count=\"true\" data-lang=\"en\">Follow @SebBrisard</a>")

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
      `(("blog-root"
         :base-directory ,sb-blog-base-directory
         :publishing-directory ,sb-blog-publishing-directory
         :base-extension "org"
         :exclude nil
         :recursive nil
         :publishing-function org-html-publish-to-html
         :auto-sitemap nil
         :html-doctype "html5"
         :html-container "div"
         :html-head ,(sb-blog-html-head 0)
         :html-head-extra ,sb-blog-html-head-extra
         :html-head-include-default-style nil
         :html-head-include-scripts nil
         :html-preamble nil
         :html-preamble ,(sb-blog-html-preamble 0)
         :html-postamble ,sb-blog-html-postamble
         :section-numbers nil
         :with-toc nil
         :language "en"
         )
        ("blog-pages"
         :base-directory ,sb-blog-pages-base-directory
         :publishing-directory ,sb-blog-pages-publishing-directory
         :base-extension "org"
         :exclude nil
         :recursive t
         :publishing-function org-html-publish-to-html
         :auto-sitemap nil
         :sitemap-sort-files chronologically
         :html-doctype "html5"
         :html-container "div"
         :html-head ,(sb-blog-html-head 1)
         :html-head-extra ,sb-blog-html-head-extra
         :html-head-include-default-style nil
         :html-head-include-scripts nil
         :html-preamble ,(sb-blog-html-preamble 1)
         :html-postamble ,sb-blog-html-postamble
         :section-numbers nil
         :with-toc nil
         :language "en"
         )
        ("blog-posts"
         :base-directory ,sb-blog-posts-base-directory
         :publishing-directory ,sb-blog-posts-publishing-directory
         :base-extension "org"
         :exclude nil
         :recursive t
         :publishing-function org-html-publish-to-html
         :auto-sitemap nil
         :sitemap-filename "archives.org"
         :sitemap-title "Blog archive"
         :sitemap-sort-files anti-chronologically
         :sitemap-file-entry-format "%d -- %t"
         :html-doctype "html5"
         :html-container "div"
         :html-head ,(sb-blog-html-head 1)
         :html-head-extra ,sb-blog-html-head-extra
         :html-head-include-default-style nil
         :html-head-include-scripts nil
         :html-preamble ,(sb-blog-html-preamble 1)
         :html-postamble ,sb-blog-html-postamble
         :section-numbers nil
         :with-toc nil
         :language "en"
         )
        ("blog-images"
         :base-directory ,sb-blog-base-directory
         :publishing-directory ,sb-blog-publishing-directory
         :base-extension "jpg\\|gif\\|png"
         :recursive t
         :publishing-function org-publish-attachment)
        ("blog-css"
         :base-directory ,sb-blog-css-base-directory
         :publishing-directory ,sb-blog-css-publishing-directory
         :base-extension "css"
         :recursive t
         :publishing-function org-publish-attachment)
        ("blog"
         :components ("blog-root"
                      "blog-pages"
                      "blog-posts"
                      "blog-images"
                      "blog-css"))))
