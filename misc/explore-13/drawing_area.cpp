#include <gtk/gtk.h>

// Callback for the draw event
static gboolean on_draw(GtkWidget *widget, cairo_t *cr, gpointer user_data) {
    // Set the background color
    cairo_set_source_rgb(cr, 1.0, 1.0, 1.0); // White
    cairo_paint(cr);

    // Draw a rectangle
    cairo_set_source_rgb(cr, 0.0, 0.0, 1.0); // Blue
    cairo_rectangle(cr, 50, 50, 200, 100);   // x, y, width, height
    cairo_fill(cr);

    return FALSE; // Return FALSE to propagate the event further if necessary
}

int main(int argc, char *argv[]) {
    // Initialize GTK
    gtk_init(&argc, &argv);

    // Create the main window
    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "GTK+ Drawing Area Example");
    gtk_window_set_default_size(GTK_WINDOW(window), 500, 400);

    // Connect the "destroy" signal to quit the application
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    // Create a drawing area
    GtkWidget *drawing_area = gtk_drawing_area_new();
    gtk_widget_set_size_request(drawing_area, 500, 400);

    // Connect the "draw" signal to the callback
    g_signal_connect(drawing_area, "draw", G_CALLBACK(on_draw), NULL);

    // Add the drawing area to the window
    gtk_container_add(GTK_CONTAINER(window), drawing_area);

    // Show all widgets
    gtk_widget_show_all(window);

    // Run the GTK main loop
    gtk_main();

    return 0;
}

