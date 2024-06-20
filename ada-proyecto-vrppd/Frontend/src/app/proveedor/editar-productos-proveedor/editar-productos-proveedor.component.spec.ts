import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditarProductosProveedorComponent } from './editar-productos-proveedor.component';

describe('EditarProductosProveedorComponent', () => {
  let component: EditarProductosProveedorComponent;
  let fixture: ComponentFixture<EditarProductosProveedorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EditarProductosProveedorComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EditarProductosProveedorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
