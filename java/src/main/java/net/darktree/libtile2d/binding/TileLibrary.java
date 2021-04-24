package net.darktree.libtile2d.binding;

import com.sun.jna.Callback;
import com.sun.jna.Library;
import com.sun.jna.Pointer;

// Auto generated by bindgen.py 
public interface TileLibrary extends Library {

    /// Initialize LibTile2d
    boolean engine_init();

    /// Initialize LibTile2d
    void engine_exit();

    /// Create and open new Window object
    Pointer window_new( String name, int width, int height );

    /// Check if the window was created
    boolean window_verify( Pointer window );

    /// Delete and close a window object
    void window_free( Pointer window );

    /// Add layer (or layer group) to window
    void window_add_layer( Pointer window, Pointer layer );

    /// Delete and close a window object
    void window_set_resource_handle( Pointer resource_handle );

    /// Create and open new Window object
    Pointer resource_handle_new();

    /// Delete and close a window object
    void resource_handle_free( Pointer resource_handle );

    /// Create new Resource object
    Pointer resource_create( Pointer resource_handle, int tile );

    /// Add light component to resource
    void resource_add_light( byte r, byte g, byte b );

    /// Add texture component to resource
    void resource_add_texture( int id, Pointer data );

    /// Add texture animation frame
    void resource_add_frame( int id );

    /// Create new Layer object
    Pointer layer_new( Pointer parent );

    /// Delete Layer object
    void layer_free( Pointer layer );

    /// Set layer's z-index
    void layer_set_index( Pointer layer, long index );

    /// Set layer's x, y, and rotation
    void layer_set_position( Pointer layer, float x, float y, float r );

    /// Set tile map
    void layer_set_map( Pointer layer, Pointer map );

    /// Get layer's z-index
    long layer_get_index( Pointer layer );

    /// Get layer's position x
    float layer_get_posx( Pointer layer );

    /// Get layer's position y
    float layer_get_posy( Pointer layer );

    /// Get layer's rotation
    float layer_get_rotation( Pointer layer );

    /// Create new tile map given a map trait
    Pointer map_new( byte trait );

    /// Set tile at position, this expands the map if required
    void map_set_tile( Pointer map, int x, int y, int tile );

    /// Delete tile map
    void map_free( Pointer map );

}
