import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NavbarBipComponent } from './navbar-bip.component';

describe('NavbarBipComponent', () => {
  let component: NavbarBipComponent;
  let fixture: ComponentFixture<NavbarBipComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NavbarBipComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(NavbarBipComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
