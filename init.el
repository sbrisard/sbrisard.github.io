(defvar sb-blog-path-to-blog (concat sb-path-to-local-documents "blog/"))
(defvar sb-blog-path-to-blog-base-directory (concat sb-blog-path-to-blog "org/"))
(defvar sb-blog-path-to-blog-publishing-directory (concat sb-blog-path-to-blog "html/"))

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
      `(("blog-orgfiles"
         :html-doctype "html5"
         :html-head-include-default-style nil
         :html-head-include-scripts nil
         :html-preamble "<a href='../pages/about.html'>About me</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href='../pages/references.html'>References</a>"
         :html-postamble "<a class='twitter-follow-button' href='https://twitter.com/SebBrisard' data-show-count='true' data-lang='en'>Follow @SebBrisard</a>"
         :base-directory ,sb-blog-path-to-blog-base-directory
         :publishing-directory ,sb-blog-path-to-blog-publishing-directory
         :base-extension "org"
         :exclude "header.*\\|navbar.*"
         :recursive t
         :publishing-function org-html-publish-to-html
         :section-numbers nil
         :auto-sitemap nil
         :sitemap-sort-files chronologically
         :with-toc nil)
        ("blog-images"
         :base-directory ,sb-blog-path-to-blog-base-directory
         :publishing-directory ,sb-blog-path-to-blog-publishing-directory
         :base-extension "jpg\\|gif\\|png"
         :recursive t
         :publishing-function org-publish-attachment)
        ("blog-other"
         :base-directory ,sb-blog-path-to-blog-base-directory
         :publishing-directory ,sb-blog-path-to-blog-publishing-directory
         :base-extension "css"
         :recursive t
         :publishing-function org-publish-attachment)
        ("blog"
         :components ("blog-orgfiles" "blog-images" "blog-other"))))
