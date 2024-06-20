import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BienvenidoProveedorComponent } from './bienvenido-proveedor.component';

describe('BienvenidoProveedorComponent', () => {
  let component: BienvenidoProveedorComponent;
  let fixture: ComponentFixture<BienvenidoProveedorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BienvenidoProveedorComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(BienvenidoProveedorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
