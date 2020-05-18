package Chess;

import javax.swing.*;
import javax.swing.event.*;
import javax.swing.text.html.*;

import java.awt.*;
import java.io.*;
import java.net.*;

public class HTMLModule {

    JEditorPane html;

    /**
     * HtmlModule Constructor
     * @param panel
     * @param path
     */
    public HTMLModule(JPanel panel, String path) {
        System.out.println("HTMLModule ctor");
        try {
            URL url = null;
            try {
                url = getClass().getResource(path);
                if (url == null) {
                    System.out.println("problem");
                }
            } catch (Exception e) {
                System.out.println("Failed to open " + path);
            }

            if (url == null) {
                System.out.println("url is null");
            }
            if (url != null) {
                html = new JEditorPane(url);
                html.setEditable(false);
                html.addHyperlinkListener(createHyperLinkListener());

                JScrollPane scroller = new JScrollPane();
                JViewport vp = scroller.getViewport();
                vp.add(html);
                panel.add(scroller, BorderLayout.CENTER);
            }
        } catch (MalformedURLException e) {
            System.out.println("Malformed URL: " + e);
        } catch (IOException e) {
            System.out.println("IOException: " + e);
        }
    }

    public HyperlinkListener createHyperLinkListener() {
        return new HyperlinkListener() {
            public void hyperlinkUpdate(HyperlinkEvent e) {
                if (e.getEventType() == HyperlinkEvent.EventType.ACTIVATED) {
                    if (e instanceof HTMLFrameHyperlinkEvent) {
                        ((HTMLDocument) html.getDocument()).processHTMLFrameHyperlinkEvent(
                                (HTMLFrameHyperlinkEvent) e);
                    } else {
                        try {
                            html.setPage(e.getURL());
                        } catch (IOException ioe) {
                            System.out.println("IOE: " + ioe);
                        }
                    }
                }
            }
        };
    }

}
